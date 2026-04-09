# database/ — SQLite to Microsoft Access Conversion

## Overview

The vet clinic database is built and stored as SQLite (`vet_clinic.db`). To use it in Microsoft Access, you have two options:

---

## Option 1: Export to CSV and Import into Access (Recommended)

### Step 1: Export to CSV

Run the export script:
```bash
python3 database/export_to_csv.py
```

This creates CSV files in `database/csv_exports/`:
- Clients.csv
- Pets.csv
- Staff.csv
- Appointments.csv

### Step 2: Import into Access

On your Windows machine with Microsoft Access:

1. **Create a new blank Access database** (File > New > Blank database)
2. **Import each CSV file:**
   - External Data > New Data Source > From File > Text File
   - Select `Clients.csv` 
   - Choose "Create new table"
   - Repeat for Pets.csv, Staff.csv, Appointments.csv
3. **Set up relationships** (Database Tools > Relationships)
   - Clients.ClientID → Pets.ClientID
   - Pets.PetID → Appointments.PetID
   - Staff.StaffID → Appointments.StaffID

### Result
All tables in Access with all your data. Ready to use, edit, and submit.

---

## Option 2: Direct SQLite to Access Conversion (Windows Only)

If you have Windows with Microsoft Access and pypyodbc installed:

```bash
python3 database/sqlite_to_access.py
```

This creates `database/vet_clinic.accdb` directly from the SQLite database.

**Requirements:**
- Windows operating system
- Microsoft Access installed
- `pip install pypyodbc`

---

## Files

**vet_clinic.db** — SQLite database (repo proof artifact)

**vet_clinic_schema.sql** — SQL DDL to create the schema

**vet_clinic_verify.sql** — Verification queries

**export_to_csv.py** — Export to CSV files (works on any platform)

**sqlite_to_access.py** — Direct SQLite to .accdb conversion (Windows only)

---

## Truth Boundary

**Inside the repo (verifiable):**
- SQLite database with schema
- Verification queries that prove structure is correct
- CSV exports of the schema

**Outside the repo (your responsibility):**
- Opening files in Microsoft Access
- Importing CSV data
- Capturing screenshots if assignment requires them
- Final submission formatting

---

## Rule

SQLite build is proof. Access conversion is a formatting step that happens after repo work is complete.
