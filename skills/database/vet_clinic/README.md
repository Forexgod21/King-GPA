# skills/database/vet_clinic/

## Purpose

This folder contains the executable SQLite implementation of the vet clinic database assignment. It holds the schema, verification queries, and sample data load scripts that can be run directly in SQLite.

---

## Files

### vet_clinic_schema.sql
Contains the complete SQL DDL (Data Definition Language) to create the vet clinic database:
- Clients table
- Pets table
- Staff table
- Appointments table
- Referential integrity constraints (foreign keys)
- Indexes for common queries

**Usage:**
```bash
sqlite3 vet_clinic.db < vet_clinic_schema.sql
```

### vet_clinic_verify.sql
Contains SQL queries to verify:
- All tables are created correctly
- All field names and types match the schema
- Sample relationship queries work
- Data integrity checks run without errors

**Usage:**
```bash
sqlite3 vet_clinic.db < vet_clinic_verify.sql
```

### README.md
This file. Explains the folder contents and how to use them.

---

## Quick Start

1. **Create the database:**
   ```bash
   sqlite3 vet_clinic.db < vet_clinic_schema.sql
   ```

2. **Verify the schema:**
   ```bash
   sqlite3 vet_clinic.db < vet_clinic_verify.sql
   ```

3. **Open database shell:**
   ```bash
   sqlite3 vet_clinic.db
   ```

4. **Sample query in shell:**
   ```sql
   SELECT * FROM Clients;
   SELECT * FROM Appointments;
   ```

---

## How This Fits Into King-GPA

This folder represents the **execution proof** for the vet clinic database assignment.

- The schema is based on the physical model from [vet_clinic_physical_model.md](examples/vet_clinic_physical_model.md)
- The verify script proves the build works
- The `.db` file itself is verifiable proof the database exists and was built correctly
- All of this lives in the repo and can be committed as proof artifacts

---

## Truth Boundary

This folder is proof of database creation **inside the repo environment**. 

If the assignment requires exporting to Microsoft Access or capturing Design View screenshots, those are additional steps that happen outside the repo and must be documented separately.

---

## Rule

Database schema and verification live in the repo. Export and optional manual formatting steps are documented as separate, post-repo activities.
