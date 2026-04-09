# pipelines/gap_detector.md

## Purpose

The gap detector runs after classification and before any build execution begins. Its job is to identify missing inputs, incomplete materials, or unresolved placeholders that would prevent the workflow from completing correctly.

If a gap is found, it is surfaced immediately. The system does not proceed as if the gap does not exist.

---

## What the Gap Detector Checks

- **Missing assignment files** — No file was attached or provided for the assignment
- **Missing rubric or instructions** — No grading rubric, requirements list, or instructor instructions are present
- **Missing source materials** — Required datasets, starter code, templates, or reference files are absent
- **Missing project model or schema** — No physical model, ERD, database schema, or data structure was provided when one is required
- **Missing screenshots or proof artifacts** — Assignment requires evidence of software use, test output, or task completion but none exists
- **Missing software access** — Required software, platform, or environment is not available in the current environment
- **Missing required tool environment** — No compiler, runtime, database engine, or equivalent tool is accessible for execution
- **Placeholders still present in draft files** — Files contain unfilled fields such as `[Student Name]`, `[Date]`, `[Course Number]`, `TBD`, or equivalent

---

## Common Gap Types

| Assignment Type | Example Gap |
|---|---|
| Access assignment | Physical model or ERD not provided — cannot build or validate schema |
| Programming assignment | No prompt details given — cannot determine expected inputs, outputs, or logic |
| Presentation assignment | No topic, slide count, or content requirements specified |
| Paper or written assignment | Title page placeholders such as `[Your Name]` or `[Institution]` not filled in |

---

## Output Behavior

When a gap is detected, the system must:

- **Flag the missing item clearly** — Name exactly what is missing, not a vague error
- **Avoid pretending execution can continue normally** — Do not build around a missing input or substitute assumptions for real materials
- **Identify whether the gap blocks all progress or only part of the workflow** — Some gaps block the entire build; others only block a specific section or deliverable

---

## Rule

If a required input is missing, the system must surface the gap before build execution continues.
