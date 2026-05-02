# How to Use King-GPA

Purpose
- King-GPA is an academic IT support system that turns assignment requirements into organized, verifiable deliverables.

Quick start
- Place the assignment materials (instructions, files) into the `assignments/` folder.
- Create an intake manifest in `intake/` that lists required outputs and constraints.

Core workflow (what'll happen)
1. Intake — record the assignment and required deliverables.
2. Classification — pick the appropriate `skills/` module or `pipelines/` workflow.
3. Gap detection — identify missing inputs, tools, or blockers and note them in the intake manifest.
4. Execution — build outputs (code, schemas, docs) following the chosen pipeline.
5. Validation — run QA checks in `qa/` and confirm requirements are satisfied.
6. Packaging — place final artifacts into `outputs/` with any delivery notes.

Repository layout (where to look)
- `assignments/` — raw assignment source materials.
- `intake/` — manifests and extracted requirement details.
- `skills/` — modules that implement task-specific logic.
- `pipelines/` — workflow guidance and step checklists.
- `templates/` — reusable output formats.
- `outputs/` — generated deliverables.
- `qa/` — validation checklists and reports.

Agent roles
- Codex: repository builder and implementer.
- Claude: analysis and architecture reasoning.
- Copilot: in-editor scaffolding and file edits.

Important rules
- The system will not claim work is tested or verified unless that actually happened.
- Flag any blockers or manual verification steps clearly in the intake/QA files.

Next steps you can do right now
- Add your assignment to `assignments/` and create an intake manifest in `intake/`.
- If you'd like, I can: create an example manifest, scaffold a pipeline for a specific assignment type, or update the `README.md` to link to this guide.

Thank you for using King-GPA. If you want this adapted into a printable checklist or a shorter quickstart card, tell me which format you prefer.
