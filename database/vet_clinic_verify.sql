-- Vet Clinic Database Verification Queries

-- List all tables
.tables

-- Show schema for each table
.schema Clients
.schema Pets
.schema Staff
.schema Appointments

-- Select from sqlite_master to show table definitions
SELECT name, type, sql FROM sqlite_master WHERE type='table';

-- Example verification queries for relationships

-- Count records in each table
SELECT 'Clients' as TableName, COUNT(*) as RecordCount FROM Clients
UNION ALL
SELECT 'Pets', COUNT(*) FROM Pets
UNION ALL
SELECT 'Staff', COUNT(*) FROM Staff
UNION ALL
SELECT 'Appointments', COUNT(*) FROM Appointments;

-- Test Clients -> Pets relationship
SELECT 
    c.ClientID,
    c.FirstName,
    COUNT(p.PetID) as PetCount
FROM Clients c
LEFT JOIN Pets p ON c.ClientID = p.ClientID
GROUP BY c.ClientID, c.FirstName;

-- Test Appointments joins (Pet -> Staff)
SELECT 
    a.AppointmentID,
    p.PetName,
    s.FirstName || ' ' || s.LastName as StaffName,
    a.AppointmentDate
FROM Appointments a
JOIN Pets p ON a.PetID = p.PetID
JOIN Staff s ON a.StaffID = s.StaffID;
