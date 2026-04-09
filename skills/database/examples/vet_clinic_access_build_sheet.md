# skills/database/examples/vet_clinic_access_build_sheet.md

## Vet Clinic Database — Microsoft Access Build Sheet

## Purpose

This file converts the vet clinic physical model into a step-by-step Microsoft Access build sheet. It is meant to be followed directly inside Access to create the four tables, set keys and properties, and establish the relationships.

This sheet supports execution. It is not proof that execution actually happened.

---

## Build Order

Build the tables in this order so referential integrity can be enforced when relationships are created:

1. Clients
2. Pets
3. Staff
4. Appointments

---

## Table Build Instructions

### Clients

| Field Name | Data Type | Required / Optional | Key | Notes |
|---|---|---|---|---|
| ClientID | AutoNumber | Required | Primary Key | Long Integer |
| FirstName | Short Text | Required | — | Field size 50 |
| LastName | Short Text | Required | — | Field size 50 |
| PhoneNumber | Short Text | Required | — | Stored as text to preserve formatting |
| Email | Short Text | Optional | — | Field size 100 |

---

### Pets

| Field Name | Data Type | Required / Optional | Key | Notes |
|---|---|---|---|---|
| PetID | AutoNumber | Required | Primary Key | Long Integer |
| ClientID | Number | Required | Foreign Key → Clients.ClientID | Long Integer to match parent |
| PetName | Short Text | Required | — | Field size 50 |
| Species | Short Text | Required | — | Dog, Cat, etc. |
| Breed | Short Text | Optional | — | Field size 50 |
| DateOfBirth | Date/Time | Optional | — | Short Date format |

---

### Staff

| Field Name | Data Type | Required / Optional | Key | Notes |
|---|---|---|---|---|
| StaffID | AutoNumber | Required | Primary Key | Long Integer |
| FirstName | Short Text | Required | — | Field size 50 |
| LastName | Short Text | Required | — | Field size 50 |
| Role | Short Text | Required | — | Veterinarian, Technician, etc. |
| PhoneExtension | Short Text | Optional | — | Internal extension |

---

### Appointments

| Field Name | Data Type | Required / Optional | Key | Notes |
|---|---|---|---|---|
| AppointmentID | AutoNumber | Required | Primary Key | Long Integer |
| PetID | Number | Required | Foreign Key → Pets.PetID | Long Integer to match parent |
| StaffID | Number | Required | Foreign Key → Staff.StaffID | Long Integer to match parent |
| AppointmentDate | Date/Time | Required | — | General Date format |
| ReasonForVisit | Short Text | Required | — | Brief reason for visit |
| Notes | Long Text | Optional | — | Visit notes |

---

## Relationship Setup

Open the **Database Tools → Relationships** window and add the four tables. Create the following relationships and enable **Enforce Referential Integrity** on each.

- **Clients.ClientID → Pets.ClientID** (one-to-many)
- **Pets.PetID → Appointments.PetID** (one-to-many)
- **Staff.StaffID → Appointments.StaffID** (one-to-many)

---

## Screenshot Targets

Capture the following inside Microsoft Access to support the proof appendix:

- Each table opened in **Design View**:
  - Clients
  - Pets
  - Staff
  - Appointments
- All **fields visible** in each Design View screenshot
- All **data types visible** next to each field
- **Field properties visible** where relevant (primary key marker, required setting, field size for text fields, foreign key field type)
- The **Relationships window** showing all three relationships with referential integrity enabled

---

## Rule

This build sheet supports Microsoft Access execution, but it is not proof of build completion by itself.
