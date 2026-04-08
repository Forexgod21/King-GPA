# SKILLS Directory — Domain-Specific Assignment Guidance

This directory contains specialized skill files that provide best practices, requirement extraction patterns, and validation frameworks for different types of IT assignments.

---

## How to Use This System

When you provide an assignment:

1. **I automatically determine which skill applies** based on the assignment domain
2. **I load the relevant skill file** to provide domain-specific guidance
3. **I produce a Mission Brief** using patterns from that skill
4. **I validate your work** against that domain's standards

---

## Available Skills

### 🌐 [WEB-DEVELOPMENT.md](WEB-DEVELOPMENT.md)
**For:** HTML/CSS/JavaScript assignments, form building, website creation, browser validation

**Topics:**
- HTML structure requirements (forms, semantic markup, accessibility)
- CSS styling standards (layout, responsiveness, states)
- JavaScript interaction and validation
- Cross-browser testing and deployment
- Common pitfalls (hardcoded values, missing attributes, accessibility)

**Use when:** Building websites, forms, web pages, or interactive web components

---

### 🗄️ [DATABASE-DESIGN.md](DATABASE-DESIGN.md)
**For:** SQL, database design, Microsoft Access, data modeling, ERDs, query writing

**Topics:**
- Data modeling and entity identification
- Normalization (1NF, 2NF, 3NF)
- SQL queries (SELECT, INSERT, UPDATE, DELETE, JOINs)
- ER diagrams and Crow's Foot notation
- Performance and optimization
- Common pitfalls (denormalization, missing keys, improper JOINs)

**Use when:** Designing databases, writing SQL, creating data models, using Microsoft Access

---

### 📊 [MICROSOFT-OFFICE.md](MICROSOFT-OFFICE.md)
**For:** Word documents, Excel spreadsheets, PowerPoint presentations, OneNote organization

**Topics:**
- Word formatting (styles, hierarchy, citations, APA/MLA)
- Excel formulas, data validation, pivot tables
- PowerPoint presentation design and speaker notes
- Professional document standards
- Collaboration and sharing features
- Common pitfalls (manual formatting, hardcoded values, inconsistent design)

**Use when:** Creating reports in Word, data analysis in Excel, presentations in PowerPoint

---

### ☁️ [GOOGLE-WORKSPACE.md](GOOGLE-WORKSPACE.md)
**For:** Google Docs, Google Sheets, Google Slides, Google Forms, Drive organization

**Topics:**
- Collaborative document editing and comments
- Real-time spreadsheet collaboration
- Web-based presentations and presenter view
- Form design and auto-scoring
- Sharing permissions and access control
- Common pitfalls (lost work, unresolved comments, broken sharing)

**Use when:** Collaborative projects, cloud-based coursework, surveys and data collection

---

### 📄 [DOCUMENTS-DIAGRAMS.md](DOCUMENTS-DIAGRAMS.md)
**For:** PDFs, image creation/editing, Visio diagrams, infographics, wireframes, screenshots

**Topics:**
- PDF creation, merging, optimization
- Image formats, resolution, compression
- Diagram notation (Crow's Foot, UML, flowcharts)
- Infographic design and data visualization
- Wireframes and prototypes
- Accessibility in visual artifacts
- Common pitfalls (wrong format, poor resolution, unclear symbols)

**Use when:** Creating diagrams, editing images, making visual mockups, handling PDFs

---

### 📋 [GENERAL-PROJECT-MANAGEMENT.md](GENERAL-PROJECT-MANAGEMENT.md)
**For:** ANY assignment (cross-domain), planning, requirements analysis, validation, timeline management

**Topics:**
- Universal assignment analysis process
- Requirements breakdown and categorization
- Task sequencing and dependency mapping
- Effort estimation
- Rubric interpretation
- Submission readiness
- Deadline management
- Quality standards

**Use for:** Initial planning of ANY IT assignment, deadline management, rubric understanding, universal best practices

---

## Skill Selection Logic

When I receive an assignment, I determine which skill to use:

```
Is it primarily about...?

HTML/CSS/JavaScript/Web?
  → Load WEB-DEVELOPMENT.md

SQL/Databases/Access/Relational?
  → Load DATABASE-DESIGN.md

Word/Excel/PowerPoint documents?
  → Load MICROSOFT-OFFICE.md

Google Docs/Sheets/Slides/Forms?
  → Load GOOGLE-WORKSPACE.md

PDFs/Images/Diagrams/Visio/Wireframes?
  → Load DOCUMENTS-DIAGRAMS.md

Anything requires planning/validation?
  → Load GENERAL-PROJECT-MANAGEMENT.md (always)

Multiple domains?
  → Load GENERAL-PROJECT-MANAGEMENT.md + each relevant domain skill
```

---

## Skill Structure

Each SKILL.md file includes:

1. **Domain Definition** — What this skill covers
2. **Assignment Analysis Pattern** — How to break down assignments in this domain
3. **Requirement Extraction Checklist** — Questions to ask for every assignment
4. **Common Pitfalls** — What typically goes wrong and how to avoid it
5. **Validation Framework** — How to prove requirements are met
6. **Testing Checklist** — QA steps before submission
7. **Code/Work Quality Standards** — Professional execution guidelines
8. **Resources & References** — Tools and learning materials
9. **Escalation Criteria** — When to ask for help

---

## Adding New Skills

When you encounter a new IT domain/course not covered:

1. **Request a new skill** — Tell me the domain and course
2. **I'll create the SKILL.md file** following this template
3. **It gets added to this directory**
4. **It becomes part of the system going forward**

Examples of skills to add later:
- Python programming (scripting, data analysis, automation)
- Linux/Unix administration
- Networking and Security
- Project documentation and technical writing
- UX/UI Design principles
- Mobile app development
- Cloud computing (AWS, Azure, Google Cloud)
- And more as your coursework demands

---

## Workflow Example

```
You: Here's my assignment
Me: [Analyzes assignment content]
Me: [Determines: This is a web form + database design project]
Me: [Loads: WEB-DEVELOPMENT.md + DATABASE-DESIGN.md + GENERAL-PROJECT-MANAGEMENT.md]
Me: Produces Mission Brief with:
  - Form requirements from WEB-DEVELOPMENT.md patterns
  - Database requirements from DATABASE-DESIGN.md patterns
  - Overall planning from GENERAL-PROJECT-MANAGEMENT.md patterns
  - Task sequence with dependencies
  - Validation checklist
  - Timeline and gotchas

You: [Reviews mission brief]
You: Starts executing with full clarity and confidence
```

---

## Master Skill Index

| Skill | Domain | Best For |
|-------|--------|----------|
| WEB-DEVELOPMENT | HTML/CSS/JavaScript | Websites, forms, web apps |
| DATABASE-DESIGN | SQL, Access, data modeling | Databases, queries, data design |
| MICROSOFT-OFFICE | Word, Excel, PowerPoint | Reports, data analysis, presentations |
| GOOGLE-WORKSPACE | Google Docs/Sheets/Slides | Collaborative, cloud-based work |
| DOCUMENTS-DIAGRAMS | PDFs, images, diagrams, wireframes | Visual artifacts, mockups |
| GENERAL-PROJECT-MANAGEMENT | Universal | ALL assignments — planning & validation |

---

## Notes

- GENERAL-PROJECT-MANAGEMENT.md is used for EVERY assignment (it's foundational)
- Domain-specific skills are layered on top for specialized guidance
- Skills evolve — tell me what's missing or what would help
- All skills are designed to be complementary, not competitive

---

## Questions?

- **"I have an assignment type that doesn't fit these skills"** → Share it, and I'll create a new skill
- **"I don't know which skill applies"** → Share the assignment; I'll determine it
- **"A skill is missing something"** → Tell me what, and I'll add it
- **"Can I see how a skill gets used?"** → Share an assignment, and I'll show you

**Next Step:** Share your first assignment, and I'll demonstrate how these skills work in practice.
