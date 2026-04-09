# database/

## Building the Vet Clinic Database

The vet clinic database is built and verified entirely in SQLite within Codespaces.

### Create the Database

```bash
sqlite3 database/vet_clinic.db < database/vet_clinic_schema.sql
```

This command:
- Creates a new SQLite database file named `vet_clinic.db`
- Reads and executes all commands from `vet_clinic_schema.sql`
- Builds the four tables: Clients, Pets, Staff, Appointments
- Sets up foreign key relationships and constraints

### Verify the Database

```bash
sqlite3 database/vet_clinic.db < database/vet_clinic_verify.sql
```

This command:
- Connects to the existing `vet_clinic.db` file
- Lists all tables
- Shows the schema for each table
- Runs example verification queries to test relationships
- Confirms the database was built correctly

---

## Files

**vet_clinic_schema.sql** — SQLite DDL file that creates the database structure

**vet_clinic_verify.sql** — Verification queries that confirm the build is correct

**vet_clinic.db** — The actual SQLite database file (created after running schema)

---

## Converting to Microsoft Access

To use this database in Microsoft Access, run the conversion script:

```bash
python3 database/export_to_csv.py
```

This exports all 4 tables to CSV format that can be imported into Access.

See [CONVERSION.md](CONVERSION.md) for detailed import instructions.

### WARNING — CSV import does NOT finish the Access build

Exporting SQLite tables to CSV and importing them into Microsoft Access does
**not** preserve final Access-specific design settings. The following are lost
or wrongly inferred during import and must be fixed by hand in Design View:

- AutoNumber primary keys (imported as plain Number)
- Date/Time field typing (often imported as Short Text)
- Long Text vs Short Text (Notes-style fields default to Short Text)
- Required field properties
- Relationships between tables

CSV import is **only a data transfer step**. It is not proof of a correct
Access build. After import, every table must be opened in Access Design View
and corrected to match the intended schema before screenshots are taken.

See [skills/database/examples/vet_clinic_access_cleanup_after_import.md](../skills/database/examples/vet_clinic_access_cleanup_after_import.md)
for the exact cleanup steps.

---

## Truth Boundaries

**In Codespaces (repo-verified):**
- Database schema creation
- Verification queries
- SQL query execution
- Data loading
- Export to CSV or SQL dump

**Outside Codespaces (manual steps if required):**
- Import CSV into Microsoft Access
- Manual cleanup of every table in Access Design View (data types, AutoNumber, Long Text, Required, relationships)
- Screen capture of Access Design View *after* cleanup
- Any other submission format requirements

The SQLite database built in Codespaces is verifiable proof of database structure and relationships. Access conversion is a starting point only — the Access Design View must be corrected by hand before the Access build is considered complete.

---

## Example Query

To interact with the database directly:

```bash
sqlite3 database/vet_clinic.db
sqlite> SELECT * FROM Clients;
sqlite> SELECT * FROM Appointments;
sqlite> .exit
```

---

## Rule

SQLite build and verification happen in Codespaces and are committed to the repo as proof. Manual conversions or formatting are separate, optional steps.
