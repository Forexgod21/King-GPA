# Access Execution Boundary

## What can be done in the repo / Codespaces

- Build SQLite databases from `.sql` schema files
- Run verification queries
- Export tables to CSV or SQL dump
- Commit all of the above as proof of relational design

## What cannot be done in the repo / Codespaces

- Open Microsoft Access
- Set Access-specific field properties (AutoNumber, Long Text, Required, Date/Time)
- Build Access relationships in the Relationships window
- Take screenshots of Access Design View

## Important: SQLite/CSV → Access is not a finished build

Workflows that build in SQLite and then import CSV into Access **require
manual cleanup in Access Design View** before the database is considered
correct for an Access-based assignment.

CSV import will commonly produce these wrong results:

- Primary key fields imported as Number instead of AutoNumber
- Date fields imported as Short Text instead of Date/Time
- Notes / long-form fields imported as Short Text instead of Long Text
- Required properties dropped
- Relationships missing entirely

The Access file is only "done" when every table's Design View matches the
intended final schema. Screenshots taken before that cleanup are not proof
of a correct build.

See `examples/vet_clinic_access_cleanup_after_import.md` for the concrete
per-table cleanup checklist used by the vet clinic assignment.

## Rule

The repo proves the relational design.
Access Design View proves the Access build.
CSV import is the bridge between them, not the finish line.
