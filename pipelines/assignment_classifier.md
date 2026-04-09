# pipelines/assignment_classifier.md

## Assignment Classification Guide

Assignment classification happens after intake. The manifest identifies what the assignment is, and the classifier determines which skill or pipeline should execute the work.

---

## Assignment Categories

### database

**What it usually involves:**
- Database schema design
- SQL query writing
- Data modeling
- Normalization planning
- ER diagramming

**Common required outputs:**
- Schema definition (DDL)
- Query scripts
- Database documentation
- ER diagram or schema visualization

**Common software/tools:**
- SQL Server, PostgreSQL, MySQL, SQLite, or equivalent
- Database design tools (lucidchart, dbdiagram, visio)
- Query execution environment

**Common manual execution boundaries:**
- Database creation must happen in actual database software
- Data import/testing may require external tool
- ER diagrams may need to be created in design software

---

### programming

**What it usually involves:**
- Writing code in Python, Java, C++, JavaScript, or other languages
- Algorithm implementation
- Object-oriented design
- Debugging and testing

**Common required outputs:**
- Source code files
- Runtime results or test harness output
- Documentation or code comments
- Test cases or proof of functionality

**Common software/tools:**
- Language-specific compiler/interpreter
- IDE (VS Code, PyCharm, IntelliJ, etc.)
- Testing frameworks

**Common manual execution boundaries:**
- Code must be compiled/run in target language environment
- Test results must be verified in actual runtime
- Performance testing may require specific hardware

---

### web-development

**What it usually involves:**
- HTML/CSS/JavaScript implementation
- Frontend design and layout
- API integration or backend connectivity
- Responsive design

**Common required outputs:**
- HTML/CSS/JavaScript files
- Live working website or demo
- Screenshots or browser preview
- Deployment link if required

**Common software/tools:**
- Browser (Chrome, Firefox, Safari)
- Code editor
- Local server or hosting platform
- Browser developer tools

**Common manual execution boundaries:**
- Website must be tested in actual browser
- Responsive design must be verified on multiple screens
- API calls must be tested against live or test API
- Deployment must happen on actual hosting platform

---

### networking

**What it usually involves:**
- Network topology design
- IP addressing and subnetting
- Configuration documentation
- Network protocol analysis
- Cisco or Packet Tracer labs

**Common required outputs:**
- Network diagram or topology
- Configuration scripts or commands
- IP addressing plan
- Lab setup documentation
- Test results or packet captures

**Common software/tools:**
- Packet Tracer or equivalent simulator
- Network diagramming tools (Visio, Cisco IOU, GNS3)
- Wireshark or packet capture tools

**Common manual execution boundaries:**
- Packet Tracer labs must be built and tested in Packet Tracer
- Physical network testing may require actual hardware
- Configuration verification may require lab access

---

### cybersecurity

**What it usually involves:**
- Security analysis or penetration testing
- Vulnerability assessment
- Security hardening recommendations
- Incident response scenarios
- Compliance documentation

**Common required outputs:**
- Vulnerability report
- Remediation recommendations
- Security audit or assessment document
- Test results or screenshots of findings
- Compliance checklist

**Common software/tools:**
- Penetration testing tools (Metasploit, Burp Suite, etc.)
- Vulnerability scanners (Nessus, OpenVAS)
- Lab environment or sandboxed system

**Common manual execution boundaries:**
- Actual penetration testing requires access to testable systems
- Lab environment may need to be set up outside repo
- Screenshots and evidence must be captured in actual tool environment

---

### systems-analysis

**What it usually involves:**
- System requirements analysis
- Use case modeling
- System design documentation
- Process flow documentation
- Performance analysis

**Common required outputs:**
- Requirements specification document
- Use case diagrams or descriptions
- System architecture diagram
- Process flows or data flows
- Analysis report

**Common software/tools:**
- Diagramming tools (Lucidchart, Draw.io, Visio)
- Documentation tools (Word, Google Docs)
- Spreadsheets for analysis tables

**Common manual execution boundaries:**
- Diagrams may need to be created in design software
- Live system access may be required for actual analysis
- Performance testing may require actual system environment

---

### technical-writing

**What it usually involves:**
- Technical documentation
- User manuals or guides
- API documentation
- How-to guides or tutorials
- Technical reports or white papers

**Common required outputs:**
- Documentation file (Word, PDF, Markdown)
- Screenshots if needed
- Code examples if applicable
- Formatted document ready for distribution

**Common software/tools:**
- Word processor (MS Word, Google Docs)
- Markdown editor
- Screenshot tool
- PDF converter

**Common manual execution boundaries:**
- Formatting and final PDF export may require manual tool processing
- Screenshots must be captured from actual software
- Professional formatting may require manual review

---

### presentation

**What it usually involves:**
- Slide deck creation
- Presentation content organization
- Visual design
- Speaker notes
- Multimedia integration

**Common required outputs:**
- Presentation file (.pptx, .pdf, or equivalent)
- Slide deck with content
- Speaker notes
- Multimedia files if applicable
- Delivery proof (if live presentation required)

**Common software/tools:**
- PowerPoint, Google Slides, or equivalent
- Design tools if custom graphics needed
- Video/audio software if multimedia included

**Common manual execution boundaries:**
- Final presentation export may require manual tool processing
- Live presentation delivery requires actual presentation event
- Multimedia must be integrated in actual presentation software

---

### spreadsheet

**What it usually involves:**
- Data analysis using spreadsheets
- Formula writing
- Pivot table creation
- Data visualization
- Calculations and modeling

**Common required outputs:**
- Spreadsheet file (.xlsx, .csv, or equivalent)
- Data analysis results
- Charts or visualizations
- Summary report or findings
- Formulas documented if required

**Common software/tools:**
- Excel, Google Sheets, or equivalent
- Charting and visualization tools
- Statistical analysis functions

**Common manual execution boundaries:**
- Advanced formulas or macros may require tool-specific execution
- Data import/export may require manual tool processing
- Charts must be created in actual spreadsheet software

---

### unknown

**What it usually involves:**
- Assignment type cannot be determined from available information
- Requirements are ambiguous or mixed-method
- Assignment combines multiple types in unclear ways

**Common required outputs:**
- Depends on clarification

**Common software/tools:**
- Depends on clarification

**Common manual execution boundaries:**
- Cannot determine until assignment type is clarified

---

## Routing Rules

1. **Classification happens after intake** — The manifest is populated first, then the classifier determines assignment type
2. **Classification determines workflow** — Assignment type maps to the appropriate skill or pipeline (database skill, programming skill, web-dev skill, etc.)
3. **Unclear assignments marked as unknown** — If the assignment type is ambiguous or unclear, mark it as `unknown` rather than guessing. Escalate for clarification before execution begins.
4. **One assignment, one primary type** — If an assignment mixes multiple types, identify the primary type and note secondary types in the manifest
5. **Classification is reversible** — If execution begins and the type is wrong, the manifest can be updated and execution redirected

---

## Result

Clean classification keeps the workflow predictable. You know which skill to apply. You know what manual boundaries exist before building.
