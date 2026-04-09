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

## Truth Boundaries

**In Codespaces (repo-verified):**
- Database schema creation
- Verification queries
- SQL query execution
- Data loading
- Export to CSV or SQL dump

**Outside Codespaces (manual steps if required):**
- Export to Microsoft Access
- Screen capture of Access Design View
- Any other submission format requirements

The SQLite database built in Codespaces is verifiable proof of database structure and relationships. Access conversion and screenshots are optional formatting steps, not proof of completion.

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
