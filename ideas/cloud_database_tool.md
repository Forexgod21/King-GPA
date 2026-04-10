# Cloud Database Tool — Product Idea

## The Problem

- Access is desktop-only, Windows-only, doesn't scale past a few users
- SQL tools (pgAdmin, MySQL Workbench) require developer knowledge
- Airtable is simple but expensive and proprietary
- Nothing bridges the gap between "visual and easy" and "real database underneath"

## The Idea

A web-based tool that replaces Access AND gives you a real cloud database:

- Visual table designer (drag and drop, like Access Design View)
- Visual relationship builder (draw lines between tables)
- Auto-generated forms for data entry
- Real database underneath (Postgres or SQLite cloud like Turso/D1)
- Shareable with a link — no install, no Windows, works anywhere
- Export to SQL, CSV, or Access if needed
- Free tier that covers what Access does today

## Why This Wins

Access users get something modern and shareable.
Developer users get a visual layer on top of a real database.
Students get a tool that teaches relational design without fighting old software.
Small businesses get a database they don't need IT to maintain.

## Tech Stack (starting point)

- Frontend: React or Next.js
- Backend: Node.js or Python
- Database engine: Postgres (via Supabase or self-hosted) or SQLite (via Turso)
- Visual designer: Canvas-based or library like React Flow for relationship diagrams
- Auth: simple email/password or OAuth
- Hosting: Vercel / Railway / Fly.io

## MVP Scope

Version 1 only needs:

1. Create tables with fields (name, type, primary key, required)
2. Define relationships between tables
3. View data in a spreadsheet-style grid
4. Add/edit/delete rows through the grid
5. Export to SQL or CSV

That's it. No forms, no reports, no query builder yet. Just the core
"design tables visually, get a real database" loop.

## Status

Idea stage. Parked here for future build.
