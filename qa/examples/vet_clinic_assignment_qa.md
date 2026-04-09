# qa/examples/vet_clinic_assignment_qa.md

## Purpose

This file validates the current state of the vet clinic database example assignment. It records what has actually been prepared inside the repo and what still requires real execution or proof before the assignment can be treated as submission-ready.

This is a QA snapshot — it describes the real state of the work, not the planned state.

---

## What Is Complete

- Intake manifest exists — [intake/examples/vet_clinic_assignment_manifest.example.json](../../intake/examples/vet_clinic_assignment_manifest.example.json)
- Assignment is classified as **database**
- Missing physical model was identified by the gap detector
- Physical model was created — [vet_clinic_physical_model.md](../../skills/database/examples/vet_clinic_physical_model.md)
- Access build sheet was created — [vet_clinic_access_build_sheet.md](../../skills/database/examples/vet_clinic_access_build_sheet.md)
- Part 1 writeup support exists — [vet_clinic_part1_writeup_support.md](../../skills/database/examples/vet_clinic_part1_writeup_support.md)
- Part 2 writeup support exists — [vet_clinic_part2_writeup_support.md](../../skills/database/examples/vet_clinic_part2_writeup_support.md)
- Execution boundary is documented — [access_execution_boundary.md](../../skills/database/access_execution_boundary.md)
- Workflow summary exists — [vet_clinic_workflow_summary.md](../../skills/database/examples/vet_clinic_workflow_summary.md)

---

## What Is Not Complete

- **Actual Microsoft Access database build not yet proven** — No verified Access file has been produced from the build sheet
- **Screenshots not yet proven** — No Design View or Relationships window screenshots have been captured as real artifacts
- **Final submission package not yet proven** — No packaged final document with appended proof exists

---

## Current Submission Readiness

The vet clinic example is **structurally prepared but not fully submission-ready**.

All repo-side work is in place: the manifest, classification, physical model, build sheet, writeup support for both parts, execution boundary, and workflow summary exist and are consistent with each other. A student or operator can follow the existing files directly into Microsoft Access.

However, the assignment **cannot be treated as submission-ready** until:

- The database is actually built in Microsoft Access from the build sheet
- Real Design View screenshots (and the Relationships window) are captured
- The Part 2 writeup is finalized against the real build state
- The final submission package is assembled with the real proof artifacts included

Until those steps occur, this example demonstrates a prepared workflow — not a completed deliverable.

---

## Rule

QA must describe the real completion state, not the planned state.
