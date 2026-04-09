# skills/database/examples/vet_clinic_physical_model.md

## Vet Clinic Support Database — Physical Model

**Scenario:** A small veterinary clinic needs a simple relational database to track clients (pet owners), their pets, clinic staff, and appointments. This model is build-ready for Microsoft Access.

---

## Tables

```
Table Name: Clients
Purpose: Stores pet owners who bring animals to the clinic.
Primary Key: ClientID
Fields:
  - ClientID     | AutoNumber  | required | Primary key
  - FirstName    | Short Text  | required | Client first name
  - LastName     | Short Text  | required | Client last name
  - PhoneNumber  | Short Text  | required | Stored as text to preserve formatting
  - Email        | Short Text  | optional | Contact email address
Notes: One client may own many pets.
```

```
Table Name: Pets
Purpose: Stores animals brought to the clinic, linked to their owner.
Primary Key: PetID
Fields:
  - PetID         | AutoNumber  | required | Primary key
  - ClientID      | Number      | required | Foreign key -> Clients.ClientID
  - PetName       | Short Text  | required | Name of the pet
  - Species       | Short Text  | required | Dog, Cat, etc.
  - Breed         | Short Text  | optional | Breed if known
  - DateOfBirth   | Date/Time   | optional | Birth date if known
Notes: Each pet belongs to exactly one client.
```

```
Table Name: Staff
Purpose: Stores clinic staff who handle appointments.
Primary Key: StaffID
Fields:
  - StaffID         | AutoNumber  | required | Primary key
  - FirstName       | Short Text  | required | Staff first name
  - LastName        | Short Text  | required | Staff last name
  - Role            | Short Text  | required | Veterinarian, Technician, etc.
  - PhoneExtension  | Short Text  | optional | Internal extension
Notes: One staff member may handle many appointments.
```

```
Table Name: Appointments
Purpose: Stores scheduled visits linking a pet to a staff member at a date/time.
Primary Key: AppointmentID
Fields:
  - AppointmentID    | AutoNumber  | required | Primary key
  - PetID            | Number      | required | Foreign key -> Pets.PetID
  - StaffID          | Number      | required | Foreign key -> Staff.StaffID
  - AppointmentDate  | Date/Time   | required | Date and time of the visit
  - ReasonForVisit   | Short Text  | required | Brief reason (checkup, vaccination, etc.)
  - Notes            | Long Text   | optional | Additional notes from the visit
Notes: Each appointment links one pet to one staff member.
```

---

## Relationships

```
Parent Table: Clients
Child Table: Pets
Key Used: ClientID
Relationship Type: one-to-many
Notes: One client can own many pets. Every pet must belong to a client.
```

```
Parent Table: Pets
Child Table: Appointments
Key Used: PetID
Relationship Type: one-to-many
Notes: One pet can have many appointments over time.
```

```
Parent Table: Staff
Child Table: Appointments
Key Used: StaffID
Relationship Type: one-to-many
Notes: One staff member can be assigned to many appointments.
```

---

## Build Notes for Microsoft Access

- Create tables in this order to support referential integrity: **Clients → Pets → Staff → Appointments**
- Set `AutoNumber` primary keys before creating relationships
- Foreign key fields (`ClientID`, `PetID`, `StaffID` in child tables) should be `Number` with Long Integer field size to match the AutoNumber parent
- Enforce referential integrity in the Relationships window when linking tables
- Phone numbers are stored as Short Text to preserve leading zeros and formatting characters
