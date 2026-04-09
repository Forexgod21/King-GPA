# skills/database/access_execution_boundary.md

## Purpose

This file defines the execution boundary between repo-based database support work and actual Microsoft Access execution.

The repo can plan, structure, explain, and validate database work. It cannot build the actual Access file, set live properties, or capture real screenshots. Those steps must happen inside Microsoft Access on a real machine.

Keeping this boundary explicit prevents the system from treating planned work as if it were executed work.

---

## What Can Be Done in the Repo

- Assignment analysis
- Physical model planning
- Table structure planning
- Field lists
- Key relationships
- Data type planning
- Build instructions
- Writeup support
- Validation planning
- Packaging planning

---

## What Must Be Done in Microsoft Access

- Creating the actual database file
- Creating the actual tables
- Setting primary keys
- Setting required properties
- Creating relationships in the software if required
- Opening tables in Design View
- Capturing screenshots

---

## Common Proof Artifacts

- Design View screenshots
- Exported database file if available
- Final document with appended screenshots

---

## Rule

Repo planning is not the same as Microsoft Access execution. The system must keep those boundaries explicit.
