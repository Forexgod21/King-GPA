#!/usr/bin/env python3
"""
SQLite to Access Converter (vet clinic)

Builds a Microsoft Access .accdb file from the vet clinic SQLite database
with the CORRECT Access field types and real foreign key relationships.

Field type mapping:
    AutoNumber primary keys -> COUNTER
    Date/Time fields        -> DATETIME
    Long Text (Notes)       -> MEMO
    Short Text              -> TEXT(n)
    Number foreign keys     -> LONG

Relationships are created with ALTER TABLE ... ADD CONSTRAINT.

If the SQLite database is missing or empty, this script will automatically
build it from vet_clinic_schema.sql and vet_clinic_data.sql first, so a
single command produces a fully populated, correctly typed .accdb.

Installation (Windows):
    pip install pypyodbc

Usage:
    python database/sqlite_to_access.py
"""

import os
import sys
import sqlite3
import subprocess
import tempfile
from datetime import datetime

# ----------------------------------------------------------------------------
# Access schema definition
# ----------------------------------------------------------------------------
# Each table lists (column_name, access_ddl_type) in order.
# date_columns lists the columns whose SQLite TEXT values must be converted
# to Python datetime objects before being inserted into Access DATETIME fields.

TABLE_SCHEMAS = {
    "Clients": {
        "columns": [
            ("ClientID",    "COUNTER CONSTRAINT PK_Clients PRIMARY KEY"),
            ("FirstName",   "TEXT(50) NOT NULL"),
            ("LastName",    "TEXT(50) NOT NULL"),
            ("PhoneNumber", "TEXT(20) NOT NULL"),
            ("Email",       "TEXT(100)"),
        ],
        "date_columns": [],
    },
    "Staff": {
        "columns": [
            ("StaffID",        "COUNTER CONSTRAINT PK_Staff PRIMARY KEY"),
            ("FirstName",      "TEXT(50) NOT NULL"),
            ("LastName",       "TEXT(50) NOT NULL"),
            ("Role",           "TEXT(50) NOT NULL"),
            ("PhoneExtension", "TEXT(10)"),
        ],
        "date_columns": [],
    },
    "Pets": {
        "columns": [
            ("PetID",       "COUNTER CONSTRAINT PK_Pets PRIMARY KEY"),
            ("ClientID",    "LONG NOT NULL"),
            ("PetName",     "TEXT(50) NOT NULL"),
            ("Species",     "TEXT(30) NOT NULL"),
            ("Breed",       "TEXT(50)"),
            ("DateOfBirth", "DATETIME"),
        ],
        "date_columns": ["DateOfBirth"],
    },
    "Appointments": {
        "columns": [
            ("AppointmentID",   "COUNTER CONSTRAINT PK_Appointments PRIMARY KEY"),
            ("PetID",           "LONG NOT NULL"),
            ("StaffID",         "LONG NOT NULL"),
            ("AppointmentDate", "DATETIME NOT NULL"),
            ("ReasonForVisit",  "TEXT(100) NOT NULL"),
            ("Notes",           "MEMO"),
        ],
        "date_columns": ["AppointmentDate"],
    },
}

# Tables must be created in this order so foreign keys reference existing tables
TABLE_ORDER = ["Clients", "Staff", "Pets", "Appointments"]

# (constraint_name, child_table, child_column, parent_table, parent_column)
RELATIONSHIPS = [
    ("FK_Pets_Clients",        "Pets",         "ClientID", "Clients", "ClientID"),
    ("FK_Appointments_Pets",   "Appointments", "PetID",    "Pets",    "PetID"),
    ("FK_Appointments_Staff",  "Appointments", "StaffID",  "Staff",   "StaffID"),
]


# ----------------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------------

def parse_sqlite_date(value):
    """Normalize a SQLite date value to an ISO string the Access ODBC
    driver accepts for DATETIME columns. Returns None for empty values.

    The Access ODBC driver rejects native Python datetime objects with
    error 22018 ("Invalid character value for cast specification") when
    bound as parameters, but it accepts ISO date/time strings directly.
    """
    if value is None or value == "":
        return None
    if isinstance(value, datetime):
        return value.strftime("%Y-%m-%d %H:%M:%S")
    s = str(value).strip()
    # If it's a bare date like "2020-05-12", pad with a time component
    if len(s) == 10:
        s += " 00:00:00"
    return s


def ensure_sqlite_populated(sqlite_path, schema_path, data_path):
    """If the SQLite db is missing or empty, build it from schema + data."""
    needs_build = False
    if not os.path.exists(sqlite_path):
        needs_build = True
    else:
        try:
            con = sqlite3.connect(sqlite_path)
            cur = con.cursor()
            cur.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table'")
            table_count = cur.fetchone()[0]
            if table_count == 0:
                needs_build = True
            else:
                cur.execute("SELECT COUNT(*) FROM Clients")
                if cur.fetchone()[0] == 0:
                    needs_build = True
            con.close()
        except sqlite3.Error:
            needs_build = True

    if not needs_build:
        return

    print("   SQLite database is empty - building from schema + data...")
    if os.path.exists(sqlite_path):
        os.remove(sqlite_path)

    con = sqlite3.connect(sqlite_path)
    with open(schema_path, "r", encoding="utf-8") as f:
        con.executescript(f.read())
    with open(data_path, "r", encoding="utf-8") as f:
        con.executescript(f.read())
    con.commit()
    con.close()
    print("   SQLite database built and seeded")


def arrange_relationships(access_path):
    """Set the Relationships window layout in the generated .accdb so it
    opens with a clean, non-crossing arrangement:

        Clients -> Pets -> Appointments <- Staff

    Access stores per-table positions for the Relationships window as
    'X' and 'Y' Document properties (in twips) on each table in the
    'Tables' container. Setting them via DAO and then opening the
    Relationships window once with Access COM automation persists the
    layout into the .accdb file.

    This step is best-effort: if pywin32 is not installed or COM fails,
    the database itself is still correct - only the visual layout is
    affected, and the user can re-run after installing pywin32.
    """
    try:
        import win32com.client
        import pythoncom
    except ImportError:
        print("   pywin32 not installed - skipping Relationships layout")
        print("   To enable automatic layout: pip install pywin32")
        return False

    # Layout positions in twips (1440 twips = 1 inch).
    # Tables are roughly 2400 twips wide; 3000 spacing avoids overlap
    # and keeps the line endpoints clean.
    positions = [
        ("Clients",      500,  1500),
        ("Pets",         3500, 1500),
        ("Appointments", 6500, 1500),
        ("Staff",        9500, 1500),
    ]

    DB_LONG = 4               # DAO field type for CreateProperty
    AC_CMD_RELATIONSHIPS = 36 # acCmdRelationships

    print("   Arranging Relationships window layout via Access COM...")
    pythoncom.CoInitialize()
    app = None
    try:
        # DispatchEx forces a fresh hidden Access instance instead of
        # latching onto one the user might already have running.
        app = win32com.client.DispatchEx("Access.Application")
        try:
            app.Visible = False
        except Exception:
            pass

        app.OpenCurrentDatabase(access_path)
        db = app.CurrentDb()

        for table_name, x, y in positions:
            doc = db.Containers("Tables").Documents(table_name)
            for prop_name, prop_val in (("X", x), ("Y", y)):
                try:
                    doc.Properties(prop_name).Value = prop_val
                except Exception:
                    new_prop = db.CreateProperty(prop_name, DB_LONG, prop_val)
                    doc.Properties.Append(new_prop)

        # Open the Relationships window so Access loads the layout from
        # the X/Y properties we just set, then save and close it. This
        # bakes the arrangement into the .accdb file.
        try:
            app.DoCmd.RunCommand(AC_CMD_RELATIONSHIPS)
            try:
                app.DoCmd.Save()
            except Exception:
                pass
            try:
                app.DoCmd.Close()
            except Exception:
                pass
        except Exception as e:
            print(f"   Note: could not open Relationships window: {e}")
            print("   Table X/Y properties were still written.")

        app.CloseCurrentDatabase()
        print("   Relationships layout arranged and saved")
        return True

    except Exception as e:
        print(f"   Could not arrange Relationships layout: {e}")
        print("   The .accdb is still correct - this only affects the visual layout.")
        return False

    finally:
        if app is not None:
            try:
                app.Quit()
            except Exception:
                pass
        try:
            pythoncom.CoUninitialize()
        except Exception:
            pass


def create_accdb(access_path):
    """Create a blank .accdb file via VBScript + ADOX."""
    escaped = access_path.replace("'", "''")
    vbs = (
        'Set cat = CreateObject("ADOX.Catalog")\n'
        f'cat.Create "Provider=Microsoft.ACE.OLEDB.12.0;Data Source={escaped};"\n'
        'Set cat = Nothing\n'
        'WScript.Echo "OK"\n'
    )
    vbs_file = os.path.join(tempfile.gettempdir(), "create_accdb.vbs")
    with open(vbs_file, "w") as f:
        f.write(vbs)

    result = subprocess.run(
        ["cscript", "//NoLogo", vbs_file],
        capture_output=True, text=True,
    )
    os.remove(vbs_file)

    if "OK" in result.stdout and os.path.exists(access_path):
        return True
    print(f"   VBScript stdout: {result.stdout.strip()}")
    print(f"   VBScript stderr: {result.stderr.strip()}")
    return False


# ----------------------------------------------------------------------------
# Main conversion
# ----------------------------------------------------------------------------

def sqlite_to_access(sqlite_path, access_path):
    try:
        import pypyodbc
    except ImportError:
        print("pypyodbc not installed")
        print("   Run: pip install pypyodbc")
        return False

    schema_path = os.path.join(os.path.dirname(sqlite_path), "vet_clinic_schema.sql")
    data_path = os.path.join(os.path.dirname(sqlite_path), "vet_clinic_data.sql")

    # 1. Make sure SQLite has the schema and seed data
    ensure_sqlite_populated(sqlite_path, schema_path, data_path)

    if not os.path.exists(sqlite_path):
        print(f"SQLite database not found: {sqlite_path}")
        return False

    access_path = os.path.abspath(access_path)
    print(f"Converting {sqlite_path} to Access format...")
    print(f"   Target: {access_path}")

    # 2. Create the blank .accdb
    if os.path.exists(access_path):
        os.remove(access_path)
        print("   Removed existing .accdb file")

    print("   Creating blank .accdb file...")
    if not create_accdb(access_path):
        print("Failed to create .accdb file")
        print("   Make sure Microsoft Access (or the Access Database Engine) is installed")
        return False
    print("   Blank .accdb created")

    # 3. Connect to SQLite and Access
    sqlite_conn = sqlite3.connect(sqlite_path)
    sqlite_cursor = sqlite_conn.cursor()

    driver = "{Microsoft Access Driver (*.mdb, *.accdb)}"
    conn_str = f"Driver={driver};DBQ={access_path};"
    access_conn = pypyodbc.connect(conn_str)
    access_cursor = access_conn.cursor()

    try:
        # 4. Create tables with proper Access types
        for table in TABLE_ORDER:
            schema = TABLE_SCHEMAS[table]
            col_defs = ", ".join(f"{name} {ddl}" for name, ddl in schema["columns"])
            create_sql = f"CREATE TABLE {table} ({col_defs})"
            access_cursor.execute(create_sql)
            print(f"   Created table: {table}")

        # 5. Create relationships (foreign key constraints)
        for name, child_t, child_c, parent_t, parent_c in RELATIONSHIPS:
            alter_sql = (
                f"ALTER TABLE {child_t} "
                f"ADD CONSTRAINT {name} "
                f"FOREIGN KEY ({child_c}) REFERENCES {parent_t} ({parent_c})"
            )
            access_cursor.execute(alter_sql)
            print(f"   Created relationship: {name}")

        # 6. Copy data, converting date columns to real datetimes
        for table in TABLE_ORDER:
            schema = TABLE_SCHEMAS[table]
            col_names = [c[0] for c in schema["columns"]]
            date_cols = set(schema["date_columns"])

            sqlite_cursor.execute(f"SELECT {', '.join(col_names)} FROM {table}")
            rows = sqlite_cursor.fetchall()

            if not rows:
                print(f"   No rows to copy for {table}")
                continue

            placeholders = ", ".join(["?"] * len(col_names))
            cols_sql = ", ".join(col_names)
            insert_sql = f"INSERT INTO {table} ({cols_sql}) VALUES ({placeholders})"

            for row in rows:
                converted = []
                for col_name, value in zip(col_names, row):
                    if col_name in date_cols:
                        converted.append(parse_sqlite_date(value))
                    else:
                        converted.append(value)
                access_cursor.execute(insert_sql, converted)

            print(f"   Copied {len(rows)} rows to {table}")

        access_conn.commit()
        print(f"\nDone: {access_path}")
        print("   Open this file in Microsoft Access - tables, types, and relationships are ready.")
        return True

    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        try:
            access_conn.close()
        except Exception:
            pass
        try:
            sqlite_conn.close()
        except Exception:
            pass


if __name__ == "__main__":
    sqlite_path = "database/vet_clinic.db"
    access_path = r"C:\Users\cadeb\Desktop\vet_clinic.accdb"

    if sys.platform != "win32":
        print("This script is designed for Windows with Microsoft Access installed")
        print("   Use export_to_csv.py instead for cross-platform CSV export")
        sys.exit(1)

    ok = sqlite_to_access(sqlite_path, access_path)
    if ok:
        # Best-effort cosmetic step: arrange the Relationships window
        # layout in the .accdb so it opens with no crossing lines.
        # Failure here does not fail the build.
        arrange_relationships(access_path)
    sys.exit(0 if ok else 1)
