# skills/database/examples/vet_clinic_workflow_summary.md

## Purpose

This file summarizes the full King-GPA workflow for the vet clinic database example, from intake through final packaging. It shows what has already been prepared inside the repo and what still requires real execution outside the repo runtime.

It exists so the state of the example is visible at a glance and the remaining manual steps cannot be quietly skipped.

---

## Workflow Path

1. **Intake manifest created** — Assignment captured in `intake/examples/vet_clinic_assignment_manifest.example.json`
2. **Assignment classified as database** — Routed to the database skill based on `pipelines/assignment_classifier.md`
3. **Missing physical model detected** — Gap detector flagged the missing model before execution per `pipelines/gap_detector.md`
4. **Physical model created** — Four-table relational model produced for Clients, Pets, Staff, and Appointments
5. **Access build sheet created** — Physical model converted into step-by-step Microsoft Access build instructions
6. **Part 1 writeup support created** — Conceptual writeup guidance covering database terms, relational concepts, Access objects, and the five-step design method
7. **Part 2 writeup support created** — Narrative guidance for explaining the actual Access build
8. **Execution boundary identified** — Repo-based work separated from work that must happen inside Microsoft Access
9. **Final packaging can occur only after actual Access build and screenshots exist** — Per `pipelines/output_packaging.md`, nothing is packaged as complete until real proof artifacts are captured

---

## Current Known Blocker

- **Microsoft Access execution and screenshots must still happen outside the repo runtime.** The repo has produced the physical model, the build sheet, and the writeup support — but the actual database file, the live tables, the configured relationships, and the Design View screenshots do not yet exist and cannot be produced inside the repo.

---

## Files Used in This Example

- [intake/examples/vet_clinic_assignment_manifest.example.json](../../../intake/examples/vet_clinic_assignment_manifest.example.json) — Intake manifest
- [skills/database/examples/vet_clinic_physical_model.md](vet_clinic_physical_model.md) — Physical model
- [skills/database/examples/vet_clinic_access_build_sheet.md](vet_clinic_access_build_sheet.md) — Microsoft Access build sheet
- [skills/database/examples/vet_clinic_part1_writeup_support.md](vet_clinic_part1_writeup_support.md) — Part 1 writeup support
- [skills/database/examples/vet_clinic_part2_writeup_support.md](vet_clinic_part2_writeup_support.md) — Part 2 writeup support

Supporting doctrine and pipeline files referenced by this workflow:

- [skills/database/skill.md](../skill.md) — Database skill definition
- [skills/database/access_execution_boundary.md](../access_execution_boundary.md) — Repo vs Access boundary
- [skills/database/physical_model_template.md](../physical_model_template.md) — Reusable physical model template
- [pipelines/assignment_classifier.md](../../../pipelines/assignment_classifier.md) — Classification
- [pipelines/gap_detector.md](../../../pipelines/gap_detector.md) — Gap detection
- [pipelines/output_packaging.md](../../../pipelines/output_packaging.md) — Final packaging

---

## Rule

A complete workflow summary must show both what has been prepared and what still requires real execution or proof.
