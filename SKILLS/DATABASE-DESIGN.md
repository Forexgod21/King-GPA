# SKILL.md — Database Design & SQL

## Domain
Database concepts: Relational design, SQL (SELECT, INSERT, UPDATE, DELETE), database normalization, Microsoft Access, data modeling, ERDs, query optimization

## When to Use
- Any database design or SQL assignment (Access, SQL Server, MySQL, etc.)
- Data modeling and Entity-Relationship Diagram (ERD) projects
- SQL query writing and optimization
- Database normalization exercises
- Real-world data scenario projects

---

## Assignment Analysis Pattern for Database Design

When analyzing a database assignment:

### 1. **Data Model Requirements**
   - Entity identification (what data entities exist?)
   - Attributes for each entity
   - Relationships between entities (1:1, 1:N, M:N)
   - Primary keys and candidate keys
   - Foreign key constraints
   - Data types and constraints (NOT NULL, UNIQUE, etc.)

### 2. **Normalization Requirements**
   - Target normalization form (1NF, 2NF, 3NF, BCNF)
   - Functional dependencies
   - Anomalies to avoid (insertion, update, deletion)
   - Table decomposition if needed
   - Join requirements based on normalized structure

### 3. **SQL Query Requirements**
   - SELECT queries with WHERE, ORDER BY, GROUP BY
   - JOIN operations (INNER, LEFT, RIGHT, FULL)
   - Aggregate functions (COUNT, SUM, AVG, MAX, MIN)
   - Subqueries and common table expressions
   - INSERT, UPDATE, DELETE operations
   - Transaction handling if needed

### 4. **Database Implementation Requirements**
   - Table creation with constraints
   - Index creation for performance
   - Data insertion and population
   - Query optimization
   - Backup and recovery (if applicable)
   - User permissions and security

### 5. **Documentation Requirements**
   - ER Diagram (Crow's Foot notation typically)
   - Data dictionary
   - Query documentation
   - Screenshots or test results
   - Design rationale and decisions

---

## Requirement Extraction Checklist

For database missions, extract:

- [ ] **Entities & Attributes**
  - [ ] List all entities (tables)
  - [ ] Identify attributes for each entity
  - [ ] Determine attribute data types
  - [ ] Identify constraints (NOT NULL, UNIQUE, DEFAULT)
  - [ ] Map real-world concepts to database design

- [ ] **Relationships**
  - [ ] Identify relationship types (1:1, 1:N, M:N)
  - [ ] Determine cardinality (min/max occurrences)
  - [ ] Plan for foreign keys and referential integrity
  - [ ] Handle junction tables for M:N relationships
  - [ ] Define relationship optionality (required vs. optional)

- [ ] **Normalization**
  - [ ] Current form and target form
  - [ ] Identify functional dependencies
  - [ ] Detect and eliminate redundancy
  - [ ] Eliminate anomalies
  - [ ] Verify compliance with target normalization level

- [ ] **SQL Queries**
  - [ ] Required query types (SELECT, INSERT, UPDATE, DELETE)
  - [ ] Filtering and WHERE clause requirements
  - [ ] Join requirements between tables
  - [ ] Aggregation and GROUP BY needs
  - [ ] Sorting and ORDER BY requirements
  - [ ] Complex queries or subquery needs

- [ ] **Testing & Validation**
  - [ ] Sample data requirements
  - [ ] Query execution verification
  - [ ] Result accuracy validation
  - [ ] Performance requirements
  - [ ] Edge cases and boundary conditions

---

## Common Pitfalls in Database Assignments

### Data Modeling Pitfalls
- ❌ Storing related data in single table (violates normalization)
- ❌ Missing primary keys on entities
- ❌ Not identifying M:N relationships (needs junction table)
- ❌ Wrong relationship cardinality (1:N vs. M:N confusion)
- ❌ Storing calculated/derived data (should be computed, not stored)

**Fix:** Require primary key on every table. Draw ER diagram FIRST before creating tables.

### Normalization Pitfalls
- ❌ Repeating groups (violates 1NF)
  ```
  ❌ BAD: StudentCourses = "CS101, MATH201, ENG101"
  ✅ GOOD: Separate StudentEnrollment table
  ```
- ❌ Partial dependency (violates 2NF)
  ```
  ❌ BAD: (StudentID, CourseID) → StudentName (depends only on StudentID)
  ✅ GOOD: Split into Students and Enrollments tables
  ```
- ❌ Transitive dependency (violates 3NF)
  ```
  ❌ BAD: StudentID → DepartmentID → DepartmentName (chain)
  ✅ GOOD: Separate Departments table
  ```

**Fix:** Test normalization formally. Create a dependency diagram.

### SQL Query Pitfalls
- ❌ SELECT * without justifying (performance, security)
- ❌ Missing WHERE clause on DELETE/UPDATE (deletes everything!)
- ❌ Wrong JOIN type causing duplicate rows
- ❌ Forgetting NULL handling in comparisons
- ❌ Not indexing frequently queried columns
- ❌ Case sensitivity issues in WHERE clauses

**Fix:** Always specify column names. Test queries on sample data first. Use WHERE clauses defensively.

### Design Pitfalls
- ❌ No primary key defined
- ❌ No foreign key constraints (orphaned records possible)
- ❌ Wrong data type (VARCHAR(10) for future expansions)
- ❌ Not considering growth (will this scale?)
- ❌ Ignoring business rules in constraints

**Fix:** Define constraints explicitly. Document why each data type was chosen.

### Access-Specific Pitfalls (if using Microsoft Access)
- ❌ Tables not properly normalized in Access
- ❌ Field names with spaces or special characters (harder to query)
- ❌ Using Text for numeric data (breaks sorting/math)
- ❌ Not setting primary keys in Access
- ❌ Relationships not enforced in the GUI

**Fix:** Use Access relationship designer to visualize. Test enforce referential integrity option.

---

## Validation Framework

### Data Model Validation
```
Entity: Student
  Attributes: StudentID (PK), Name, Email, Major
  Relationships: Enrolls in Courses (1:N)
  
✅ Each attribute assigned proper data type
✅ StudentID is unique (primary key)
✅ Email uniqueness constraint if required
✅ Relationships map to foreign keys
```

### Normalization Validation
```
Table: Enrollment (StudentID, CourseID, Grade, CourseName)

Normalization Check:
✅ 1NF: No repeating groups (each cell atomic)
✅ 2NF: No partial dependencies (Grade depends on StudentID + CourseID)
❌ 3NF: CourseName depends on CourseID only (not on composite key)
  → VIOLATES 3NF: Move CourseName to Courses table
```

### Query Validation
```
Query: "Find all students enrolled in CS101 with grade > 80"

Expected Result: [List of students matching criteria]
Execution Check:
✅ Query executes without error
✅ Results match expected output
✅ No duplicate rows
✅ Correct data types in result
```

---

## Code Quality Standards for Database Work

### Database Design Standards
- Each table has a primary key
- Foreign keys defined for all relationships
- Normalized to at least 3NF (unless justified)
- Constraints enforce business rules
- Clear, consistent naming (singular table names, underscore_separated columns)
- Documentation of design decisions

### SQL Standards
- Consistent formatting (uppercase keywords, lowercase table/column names)
- Comments explaining complex queries
- Parameterized queries for security (if applicable)
- No SELECT * (specify columns needed)
- Proper error handling and validation
- Transaction handling for multi-step operations

### ER Diagram Standards
- Crow's Foot notation (correctly used)
- All entities labeled clearly
- All relationships identified with cardinality
- Primary and foreign keys marked
- Optional/mandatory relationships shown
- Legend if using non-standard symbols

---

## Testing Checklist (Database)

Before marking complete:

- [ ] **Data Model**
  - [ ] ER Diagram is complete and accurate ✓
  - [ ] All entities identified ✓
  - [ ] All relationships shown ✓
  - [ ] Cardinality correctly marked ✓
  - [ ] Primary keys identified ✓

- [ ] **Normalization**
  - [ ] Meets target normalization form (1NF/2NF/3NF) ✓
  - [ ] No repeating groups (if 1NF required) ✓
  - [ ] No partial dependencies (if 2NF required) ✓
  - [ ] No transitive dependencies (if 3NF required) ✓
  - [ ] Design rationale documented ✓

- [ ] **Database Implementation**
  - [ ] All tables created correctly ✓
  - [ ] Primary keys enforced ✓
  - [ ] Foreign keys enforced ✓
  - [ ] Constraints (NOT NULL, UNIQUE) applied ✓
  - [ ] Sample data inserted successfully ✓

- [ ] **SQL Queries**
  - [ ] SELECT queries return correct results ✓
  - [ ] WHERE clauses filter properly ✓
  - [ ] JOINs produce correct row counts ✓
  - [ ] INSERT/UPDATE/DELETE work without errors ✓
  - [ ] Queries handle NULLs correctly ✓

- [ ] **Documentation**
  - [ ] Data dictionary complete ✓
  - [ ] Query documentation clear ✓
  - [ ] Screenshots or test results included ✓
  - [ ] Design decisions explained ✓

---

## Resources & References

- **SQL Learning:** MODE Analytics SQL Tutorial
- **ER Diagrams:** Lucidchart Crow's Foot Notation
- **Normalization:** Database Normalization Explained
- **Microsoft Access:** Microsoft Access Official Docs
- **SQL Optimization:** Query Optimization Best Practices

---

## When to Escalate to Commander

- Complex data warehouse design
- Performance requirements (query optimization under SLA)
- Multi-database synchronization
- Complex business rule enforcement
- Security and audit requirements
