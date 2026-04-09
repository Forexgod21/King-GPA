# templates/database_physical_model_checklist.md

## Purpose

This file is a reusable checklist for reviewing a physical database model before build execution starts. It is copied per assignment and filled in during model review — not edited in place.

Its job is to confirm the model is clear enough to build directly, without guesswork, before anyone opens Microsoft Access or any other database tool.

---

## Table Structure Checks

- [ ] Every table has a clear name
- [ ] Every table has a clear purpose
- [ ] Duplicate or unnecessary tables are removed
- [ ] Table scope matches the assignment scenario

---

## Key Structure Checks

- [ ] Every table has a primary key
- [ ] Foreign keys exist where relationships require them
- [ ] Foreign keys point to the correct parent table
- [ ] Key naming stays clear and consistent

---

## Field Quality Checks

- [ ] Field names are clear
- [ ] Data types fit the intended use
- [ ] Required vs optional fields are identified where possible
- [ ] Fields do not mix unrelated purposes

---

## Relationship Checks

- [ ] Parent and child tables are correctly identified
- [ ] Relationship direction is clear
- [ ] One-to-many structure is used where appropriate
- [ ] Relationships make sense for the scenario

---

## Build-Readiness Checks

- [ ] Model is clear enough to build without guessing
- [ ] Access-friendly data types are identified if needed
- [ ] Missing decisions are flagged before build starts
- [ ] Model is ready to convert into a build sheet

---

## Rule

A physical model is not build-ready until the table structure, keys, fields, and relationships are clear enough to execute without guesswork.
