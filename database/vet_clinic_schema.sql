-- Vet Clinic Database Schema
-- SQLite implementation with four tables and referential integrity

PRAGMA foreign_keys = ON;

CREATE TABLE Clients (
    ClientID INTEGER PRIMARY KEY,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    PhoneNumber TEXT NOT NULL,
    Email TEXT
);

CREATE TABLE Pets (
    PetID INTEGER PRIMARY KEY,
    ClientID INTEGER NOT NULL,
    PetName TEXT NOT NULL,
    Species TEXT NOT NULL,
    Breed TEXT,
    DateOfBirth TEXT,
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID)
);

CREATE TABLE Staff (
    StaffID INTEGER PRIMARY KEY,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    Role TEXT NOT NULL,
    PhoneExtension TEXT
);

CREATE TABLE Appointments (
    AppointmentID INTEGER PRIMARY KEY,
    PetID INTEGER NOT NULL,
    StaffID INTEGER NOT NULL,
    AppointmentDate TEXT NOT NULL,
    ReasonForVisit TEXT NOT NULL,
    Notes TEXT,
    FOREIGN KEY (PetID) REFERENCES Pets(PetID),
    FOREIGN KEY (StaffID) REFERENCES Staff(StaffID)
);
