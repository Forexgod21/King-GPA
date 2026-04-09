-- Vet Clinic Database Schema
-- SQLite implementation of the vet clinic relational database
-- Creates four tables: Clients, Pets, Staff, Appointments with referential integrity

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create Clients table
CREATE TABLE Clients (
    ClientID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    PhoneNumber TEXT NOT NULL,
    Email TEXT
);

-- Create Pets table (linked to Clients)
CREATE TABLE Pets (
    PetID INTEGER PRIMARY KEY AUTOINCREMENT,
    ClientID INTEGER NOT NULL,
    PetName TEXT NOT NULL,
    Species TEXT NOT NULL,
    Breed TEXT,
    DateOfBirth DATE,
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID)
);

-- Create Staff table
CREATE TABLE Staff (
    StaffID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    Role TEXT NOT NULL,
    PhoneExtension TEXT
);

-- Create Appointments table (linked to Pets and Staff)
CREATE TABLE Appointments (
    AppointmentID INTEGER PRIMARY KEY AUTOINCREMENT,
    PetID INTEGER NOT NULL,
    StaffID INTEGER NOT NULL,
    AppointmentDate DATETIME NOT NULL,
    ReasonForVisit TEXT NOT NULL,
    Notes TEXT,
    FOREIGN KEY (PetID) REFERENCES Pets(PetID),
    FOREIGN KEY (StaffID) REFERENCES Staff(StaffID)
);

-- Create indexes for common queries
CREATE INDEX idx_pets_client ON Pets(ClientID);
CREATE INDEX idx_appointments_pet ON Appointments(PetID);
CREATE INDEX idx_appointments_staff ON Appointments(StaffID);
CREATE INDEX idx_appointments_date ON Appointments(AppointmentDate);
