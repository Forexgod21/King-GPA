-- Vet Clinic Database Verification Queries
-- Run these queries to verify the database schema and test relationships

-- 1. SCHEMA VERIFICATION
-- Display all tables
.tables

-- 2. TABLE STRUCTURE VERIFICATION
-- Show Clients table structure
.schema Clients

-- Show Pets table structure
.schema Pets

-- Show Staff table structure
.schema Staff

-- Show Appointments table structure
.schema Appointments

-- 3. DATA INTEGRITY CHECKS
-- Count records in each table
SELECT 'Clients' as TableName, COUNT(*) as RecordCount FROM Clients
UNION ALL
SELECT 'Pets', COUNT(*) FROM Pets
UNION ALL
SELECT 'Staff', COUNT(*) FROM Staff
UNION ALL
SELECT 'Appointments', COUNT(*) FROM Appointments;

-- 4. RELATIONSHIP VERIFICATION
-- Verify Clients -> Pets relationships
SELECT 
    c.ClientID,
    c.FirstName,
    c.LastName,
    COUNT(p.PetID) as NumberOfPets
FROM Clients c
LEFT JOIN Pets p ON c.ClientID = p.ClientID
GROUP BY c.ClientID, c.FirstName, c.LastName;

-- 5. APPOINTMENT VERIFICATION
-- Show all appointments with client, pet, and staff details
SELECT 
    a.AppointmentID,
    c.FirstName || ' ' || c.LastName as ClientName,
    p.PetName,
    s.FirstName || ' ' || s.LastName as StaffName,
    a.AppointmentDate,
    a.ReasonForVisit
FROM Appointments a
JOIN Pets p ON a.PetID = p.PetID
JOIN Clients c ON p.ClientID = c.ClientID
JOIN Staff s ON a.StaffID = s.StaffID
ORDER BY a.AppointmentDate;

-- 6. FOREIGN KEY CONSTRAINT CHECK
-- Test referential integrity by checking for orphaned records
SELECT 'Orphaned Pets (no Client)' as Issue, COUNT(*) as Count
FROM Pets WHERE ClientID NOT IN (SELECT ClientID FROM Clients)
UNION ALL
SELECT 'Orphaned Appointments (no Pet)', COUNT(*)
FROM Appointments WHERE PetID NOT IN (SELECT PetID FROM Pets)
UNION ALL
SELECT 'Orphaned Appointments (no Staff)', COUNT(*)
FROM Appointments WHERE StaffID NOT IN (SELECT StaffID FROM Staff);
