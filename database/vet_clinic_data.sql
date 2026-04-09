-- Vet Clinic Sample Data
-- Fake data for the vet clinic assignment

INSERT INTO Clients (ClientID, FirstName, LastName, PhoneNumber, Email) VALUES
(1, 'Sarah', 'Johnson', '555-0101', 'sarah.johnson@email.com'),
(2, 'Michael', 'Chen', '555-0102', 'mchen@email.com'),
(3, 'Emily', 'Rodriguez', '555-0103', 'emily.r@email.com'),
(4, 'David', 'Thompson', '555-0104', NULL),
(5, 'Jessica', 'Williams', '555-0105', 'jwilliams@email.com');

INSERT INTO Staff (StaffID, FirstName, LastName, Role, PhoneExtension) VALUES
(1, 'Amanda', 'Foster', 'Veterinarian', '101'),
(2, 'Robert', 'Kim', 'Veterinarian', '102'),
(3, 'Lisa', 'Patel', 'Vet Technician', '201'),
(4, 'Mark', 'Davis', 'Receptionist', '301');

INSERT INTO Pets (PetID, ClientID, PetName, Species, Breed, DateOfBirth) VALUES
(1, 1, 'Bella', 'Dog', 'Golden Retriever', '2020-05-12'),
(2, 1, 'Max', 'Cat', 'Maine Coon', '2019-08-23'),
(3, 2, 'Charlie', 'Dog', 'Beagle', '2021-03-15'),
(4, 3, 'Luna', 'Cat', 'Siamese', '2022-01-08'),
(5, 4, 'Rocky', 'Dog', 'German Shepherd', '2018-11-30'),
(6, 5, 'Daisy', 'Rabbit', 'Holland Lop', '2023-02-14'),
(7, 5, 'Oliver', 'Cat', 'Tabby', '2020-09-19');

INSERT INTO Appointments (AppointmentID, PetID, StaffID, AppointmentDate, ReasonForVisit, Notes) VALUES
(1, 1, 1, '2026-04-10 09:00:00', 'Annual checkup', 'Bella is in great health. Weight stable at 65 lbs. All vaccinations up to date. Recommended dental cleaning at next visit. Owner reports normal appetite and activity level.'),
(2, 2, 1, '2026-04-10 10:30:00', 'Vaccination', 'Administered FVRCP booster. No adverse reactions observed during the 15 minute post-vaccination monitoring period.'),
(3, 3, 2, '2026-04-11 14:00:00', 'Limping on left front paw', 'Examined paw and found small thorn embedded in the central pad. Removed thorn and cleaned wound thoroughly. Prescribed amoxicillin for 7 days. Recheck in one week.'),
(4, 4, 2, '2026-04-12 11:15:00', 'Dental cleaning', 'Full dental cleaning performed under general anesthesia. Removed significant tartar buildup from canines and molars. No extractions needed. Recovery from anesthesia was uneventful.'),
(5, 5, 1, '2026-04-13 08:30:00', 'Annual checkup', 'Senior dog wellness exam. Mild arthritis noted in both hips. Started on joint supplement. Blood work shows normal kidney and liver function. Recommended switching to senior diet.'),
(6, 6, 2, '2026-04-14 13:00:00', 'New pet exam', 'First visit for Daisy. Healthy one year old rabbit. Discussed proper diet, housing requirements, and exercise needs with owner. Provided handouts on rabbit care.'),
(7, 7, 1, '2026-04-15 15:30:00', 'Vomiting', 'Cat presented with intermittent vomiting for 2 days. Physical examination unremarkable. Prescribed bland diet and anti nausea medication. Owner instructed to recheck in 3 days if symptoms persist.'),
(8, 1, 2, '2026-04-16 10:00:00', 'Skin irritation', 'Bella developed a hot spot on her left flank. Shaved the affected area, cleaned with antiseptic, and applied topical treatment. Owner to continue treatment at home twice daily.'),
(9, 3, 1, '2026-04-17 09:30:00', 'Recheck on paw injury', 'Follow up examination on paw wound from thorn removal. Healing progressing well with no signs of infection. Continue antibiotics for remaining 3 days as prescribed.'),
(10, 4, 2, '2026-04-18 14:30:00', 'Vaccination', 'Annual rabies vaccination and FVRCP booster administered. No adverse reactions noted. Next vaccinations due in one year.');
