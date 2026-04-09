# skills/database/examples/vet_clinic_part2_writeup_support.md

## Purpose

This file supports the written Part 2 section of the vet clinic database assignment. Part 2 is the narrative explanation of how the physical model was translated into an actual Microsoft Access database. Its job is to describe the build process accurately — not to invent steps that did not happen.

This file does not write Part 2 for the student. It guides what the writeup should cover and where the truth boundaries are.

---

## What Part 2 Should Explain

Part 2 should clearly state that:

- A new blank database was created in Microsoft Access
- Each entity in the physical model was translated into its own table
- Field names, data types, and primary keys were set based on the model
- Required fields were configured where appropriate
- The tables were reviewed in Design View
- Screenshots were captured and appended if they actually exist

---

## Suggested Structure

A simple paragraph-form outline the student can follow:

1. **Opening paragraph** — State the purpose of Part 2: to document how the vet clinic database was built in Microsoft Access based on the physical model from Part 1.

2. **Database creation paragraph** — Explain that a new blank Access database was created and named appropriately for the assignment.

3. **Table creation paragraph** — Walk through how each of the four tables (Clients, Pets, Staff, Appointments) was created from its corresponding entity in the physical model. Mention that fields, data types, and primary keys were set to match the model.

4. **Field configuration paragraph** — Describe how required fields were marked, how foreign key fields were given matching data types, and how each table was reviewed in Design View to confirm the structure.

5. **Proof and closing paragraph** — Note that screenshots of each table in Design View were captured and appended to the final document (only if true), and close with a short statement confirming the build matches the Part 1 physical model.

---

## Required Truth Boundaries

- Do not claim screenshots exist unless they were actually captured
- Do not claim the database was built unless it was actually built in Access
- Do not confuse the build sheet with completed software execution

The build sheet at [vet_clinic_access_build_sheet.md](vet_clinic_access_build_sheet.md) is a set of instructions. Following it inside Access produces the real database. Reading it does not.

---

## Rule

Part 2 writing must match the real build state and proof artifacts.
