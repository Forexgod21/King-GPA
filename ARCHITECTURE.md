# ARCHITECTURE.md
## King-GPA System Structure

### Purpose
This document defines the basic structure of the King-GPA repo and the workflow path assignments follow through the system.

---

## Repo Structure
King-GPA should be organized around a simple operational flow:

- `docs/` = supporting project documents
- `assignments/` = raw assignment files and source materials
- `intake/` = extracted assignment details and manifests
- `skills/` = assignment-type modules and logic
- `pipelines/` = execution workflows
- `templates/` = reusable output formats
- `outputs/` = generated deliverables
- `qa/` = validation reports and requirement checks

---

## Workflow Path
Every assignment should move through this sequence:

1. **Intake**
   - assignment is added
   - instructions are read
   - required outputs are identified

2. **Classification**
   - assignment type is determined
   - proper skill or pipeline is selected

3. **Gap Detection**
   - missing files, missing models, missing inputs, or tool limits are identified

4. **Execution**
   - work begins in the correct mode
   - files, drafts, code, or structures are built

5. **Validation**
   - result is checked against assignment requirements
   - blockers or missing proof are flagged

6. **Packaging**
   - final artifacts are organized for handoff or submission

---

## Structural Rule
The repo should stay simple. Every folder must have a clear purpose tied to the workflow.

Do not add folders just because they might be useful later.
Do not create assignment-type sprawl before the workflow is stable.

---

## Skill Model
King-GPA should use skill modules to support different academic IT assignment types.

Examples:
- database assignments
- programming assignments
- web assignments
- networking assignments
- cybersecurity assignments
- academic technical writing

Each skill should eventually define:
- what it supports
- what inputs it requires
- how it executes
- how it validates output

---

## System Rule
The architecture exists to keep work controlled, visible, and repeatable.

The repo should make it easy to answer:
- what is this assignment
- what is missing
- what happens next
- what is done
- what still requires verification