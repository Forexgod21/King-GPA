# Vet Clinic — Access Cleanup After Import

## Purpose

This file documents exactly what must be corrected in Microsoft Access after
importing the vet clinic data from the SQLite/CSV build in the repo. Without
this cleanup, the Access file does not match the intended schema for the
assignment, even though the SQLite database is correct.

## Why import is not enough

When CSV files exported from SQLite are imported into Access, Access guesses
field types from the data. Those guesses are wrong in important ways:

- AutoNumber primary keys come in as plain Number
- Date fields come in as Short Text
- Long-form text fields (like Notes) come in as Short Text
- Required properties are dropped
- Relationships between tables do not exist at all

CSV import is a data transfer step. It is not a finished Access build.

## Correct final Access design for each table

### Clients

- ClientID — AutoNumber, Primary Key
- FirstName — Short Text
- LastName — Short Text
- PhoneNumber — Short Text
- Email — Short Text

### Pets

- PetID — AutoNumber, Primary Key
- ClientID — Number
- PetName — Short Text
- Species — Short Text
- Breed — Short Text
- DateOfBirth — Date/Time

### Staff

- StaffID — AutoNumber, Primary Key
- FirstName — Short Text
- LastName — Short Text
- Role — Short Text
- PhoneExtension — Short Text

### Appointments

- AppointmentID — AutoNumber, Primary Key
- PetID — Number
- StaffID — Number
- AppointmentDate — Date/Time
- ReasonForVisit — Short Text
- Notes — Long Text

## Required cleanup steps

1. Open each table in Design View.
2. Correct any wrongly inferred data types to match the lists above.
3. Set the primary key manually on each table (and change it to AutoNumber on the ID columns).
4. Set Required = Yes on fields that should not be blank.
5. Rebuild the relationships in the Access Relationships window:
   - Clients.ClientID → Pets.ClientID
   - Pets.PetID → Appointments.PetID
   - Staff.StaffID → Appointments.StaffID
6. Capture screenshots only after all of the above cleanup is complete.

## Rule

CSV import is not proof of a correct Access build. The Access Design View
must match the intended final schema before screenshots are taken.
