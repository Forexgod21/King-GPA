# skills/database/physical_model_template.md

## Purpose

This file defines a reusable template for creating a physical database model for academic assignments.

A physical model is the bridge between an assignment scenario and the actual tables that will be built in Microsoft Access or another database system. It must be clear, complete, and unambiguous so the database can be built directly from it.

---

## Required Model Elements

Every physical model must include:

- Database topic or scenario
- Table names
- Fields for each table
- Data types
- Primary keys
- Foreign keys where needed
- Relationship direction
- Nullable vs required fields if known

---

## Table Template

Copy this block once per table in the model.

```
Table Name:
Purpose:
Primary Key:
Fields:
  - field_name | data_type | required? | notes
  - field_name | data_type | required? | notes
  - field_name | data_type | required? | notes
Notes:
```

---

## Relationship Template

Copy this block once per relationship in the model.

```
Parent Table:
Child Table:
Key Used:
Relationship Type:   (one-to-one, one-to-many, many-to-many)
Notes:
```

---

## Validation Checks

- Every table has a clear purpose
- Every table has a primary key
- Foreign keys point to the correct parent table
- Field names are clear
- Data types fit the intended use
- Relationships make sense for the scenario

---

## Rule

A physical model must be clear enough that the database can be built from it without guessing.
