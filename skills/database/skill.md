# skills/database/skill.md

## Purpose

The database skill supports academic IT assignments that involve relational database design, planning, build support, and writeups. It exists to keep database work structured and to maintain a clean separation between what is planned in the repo and what must be built in actual database software.

---

## What This Skill Supports

- Relational database assignments
- Physical model to table translation
- Table and field planning
- Primary key and foreign key structure
- Data type planning
- Simple query planning
- Access-oriented academic database work
- General database project writeups

---

## Typical Inputs

- Assignment instructions
- Rubric if available
- Topic or scenario
- Physical model or schema if available
- Existing draft
- Screenshots or proof artifacts if available

---

## Typical Outputs

- Table plans
- Field lists
- Key relationships
- Data type mapping
- Access build instructions
- Database writeup support
- Validation notes
- Final artifact packaging support

---

## Execution Logic

The skill should:

- **Identify the task type** — Determine whether the assignment requires design, build support, explanation, or validation
- **Detect whether a physical model already exists** — Check provided materials before generating anything new
- **Create a model only if it is truly missing and the workflow requires one** — Do not regenerate models that already exist
- **Separate planning from execution** — Distinguish what can be planned in the repo from what must be executed in Access or other database software
- **Support both academic explanation and technical structure** — Writeups and technical plans are both valid outputs depending on the assignment

---

## Validation Logic

- Check whether tables match the model
- Check whether fields and key structure are coherent
- Check whether data types fit the intended use
- Check whether the writeup matches the actual database plan
- Check whether screenshots or proof artifacts actually exist before treating them as complete

---

## Common Boundaries

- Microsoft Access may be required outside the repo runtime
- Screenshots must be actually captured, not described or simulated
- Described structure is not the same as built structure
- Generated model is not the same as verified implementation

---

## Rule

The database skill must keep planning, explanation, execution support, and proof boundaries clear at all times.
