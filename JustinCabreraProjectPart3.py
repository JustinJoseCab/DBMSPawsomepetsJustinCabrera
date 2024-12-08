import sqlite3
import pandas as pd
sqlite3.enable_callback_tracebacks(True)
#DBMS Project Part 3 

db_connect = sqlite3.connect('project1db.db')

# Instantiate cursor object for executing queries
cursor = db_connect.cursor()

#-----------------------------------------------------------------------------------------------------------
#Question 3 (a)

#Clinic Relation
cursor.execute("DROP TABLE IF EXISTS Clinic;")
createClinicQuery = """
      CREATE TABLE IF NOT EXISTS Clinic(
      clinicNo INT CHECK(clinicNo BETWEEN 0 AND 99),
      cname TEXT,
      cAddress TEXT,
      cTelephoneNo VARCHAR UNIQUE CHECK(LENGTH(cTelephoneNo) = 10),
      staffNo TEXT CHECK(LENGTH(staffNo) = 5),
      PRIMARY KEY(clinicNo),
      FOREIGN KEY(staffNo) REFERENCES Staff(staffNo)
      );
      """
cursor.execute(createClinicQuery)

#Staff Relation
cursor.execute("DROP TABLE IF EXISTS Staff;")
createStaffQuery = """
     CREATE TABLE IF NOT EXISTS Staff(
     staffNo TEXT CHECK(LENGTH(staffNo) = 5),
     sName TEXT,
     sTelephoneNo INT UNIQUE CHECK(LENGTH(sTelephoneNo) = 10),
     sDOB  DATE,
     sPosition VARCHAR(20),
     sSalary VARCHAR(20),
     clinicNo CHECK(clinicNo BETWEEN 0 AND 99),
     PRIMARY KEY(staffNo),
     FOREIGN KEY(clinicNo) REFERENCES Clinic(clinicNo)
     );
     """
cursor.execute(createStaffQuery)

#Examination Relation
cursor.execute("DROP TABLE IF EXISTS Examination;")
createExaminationQuery = """
     CREATE TABLE IF NOT EXISTS Examination(
     examNo INT CHECK(LENGTH(examNo=8)),
     complaint TEXT,
     description TEXT,
     dateSeen DATE,
     action TEXT,
     staffNo TEXT CHECK(LENGTH(staffNo) = 5),
     petNo INT CHECK(Length(petNo = 8)),
     PRIMARY KEY(examNo),
     FOREIGN KEY(staffNo) REFERENCES Staff(staffNo),
     FOREIGN KEY(petNo) REFERENCES Pets(petNo)
     );
     """
cursor.execute(createExaminationQuery)

#Pet Relation 
cursor.execute("DROP TABLE IF EXISTS Pet;")
createPetQuery =  """
     CREATE TABLE IF NOT EXISTS Pet(
     petNo INT CHECK(Length(petNo = 8)),
     pName TEXT,
     pDOB DATE,
     pSpecies TEXT,
     pBreed TEXT,
     pColor TEXT,
     clinicNo INT CHECK(clinicNo BETWEEN 0 AND 99),
     ownerNo INT CHECK(LENGTH(ownerNo) = 5),
     PRIMARY KEY(petNo),
     FOREIGN KEY(clinicNo) REFERENCES Clinic(clinicNo),
     FOREIGN KEY(ownerNo) REFERENCES Owner(ownerNo)
     );
     """
cursor.execute(createPetQuery)

#Owner Relation 
cursor.execute("DROP TABLE IF EXISTS Owner;")
createOwnerQuery =  """
     CREATE TABLE IF NOT EXISTS Owner(
     ownerNo INT CHECK(LENGTH(ownerNo) = 5),
     oName TEXT,
     oAddress TEXT,
     oTelephoneNo INT UNIQUE CHECK(LENGTH(oTelephoneNo) = 10),
     PRIMARY KEY(ownerNo)
     );
     """
cursor.execute(createOwnerQuery)

db_connect.commit()


#-----------------------------------------------------------------------------------------------------------
#Question 3 (b)

insertClinicQuery = """
      INSERT INTO Clinic
      VALUES 
          (1, 'Pawsome #1', '123 Main St', '1234567890', '00001'),
          (2, 'Pawsome #2', '456 Park Ave', '2345678901', '00002'),
          (3, 'Pawsome #3', '789 Oak Blvd', '3456789012', '00003'),
          (4, 'Pawsome #4', '101 Pine St', '4567890123', '00004'),
          (5, 'Pawsome #5', '202 Elm Rd', '5678901234', '00005')
      ;
      """
cursor.execute(insertClinicQuery)

insertStaffQuery = """
     INSERT INTO Staff (staffNo, sName, sTelephoneNo, sDOB, sPosition, sSalary, clinicNo)
     VALUES 
         ('00001', 'Alice Charles', '9876543210', '1985-03-10', 'Veterinarian', '50000', 1),
         ('00002', 'Bob Smith ', '8765432109', '1990-07-25', 'Technician', '40000', 2),
         ('00003', 'Charlie Brown', '7654321098', '1988-11-14', 'Receptionist', '35000', 3),
         ('00004', 'Diana Ross', '6543210987', '1992-09-05', 'Manager', '60000', 4),
         ('00005', 'Eve Longoria', '5432109876', '1983-02-20', 'Assistant', '30000', 5);
"""
cursor.execute(insertStaffQuery)

insertExaminationQuery = """
     INSERT INTO Examination (examNo, complaint, description, dateSeen, action, staffNo, petNo)
     VALUES 
         (12345678, 'Limping', 'Injury to left leg', '2024-01-10', 'X-ray and rest', '00001', 12345678),
         (23456789, 'Excessive grooming', 'Skin irritation', '2024-01-12', 'Topical cream', '00002', 23456789),
         (34567890, 'Vomiting', 'Food poisoning', '2023-05-15', 'Hydration therapy', '00003', 34567890),
         (45678901, 'Diarrhea', 'Stress related', '2024-01-18', 'Dietary change', '00004', 45678901),
         (45678902, 'Lack of eating', '1 week of no food', '2024-01-25', 'Medication', '00004', 45678901),
         (56789012, 'Feather loss', 'Molting season', '2024-01-20', 'No treatment needed', '00005', 56789012);
"""
cursor.execute(insertExaminationQuery)

insertPetQuery = """
     INSERT INTO Pet (petNo, pName, pDOB, pSpecies, pBreed, pColor, clinicNo, ownerNo)
     VALUES 
         (12345678, 'Buddy', '2018-05-10', 'Dog', 'Golden Retriever', 'Golden', 1, 10001),
         (23456789, 'Milo', '2019-08-22', 'Cat', 'Siamese', 'Brown', 2, 10002),
         (34567890, 'Bella', '2017-04-12', 'Dog', 'Bulldog', 'Brindle', 3, 10003),
         (45678901, 'Luna', '2020-02-14', 'Rabbit', 'Himalayan', 'White', 4, 10004),
         (56789012, 'Charlie', '2016-11-02', 'Parrot', 'Macaw', 'Blue', 5, 10005);
"""
cursor.execute(insertPetQuery)

insertOwnerQuery = """
     INSERT INTO Owner (ownerNo, oName, oAddress, oTelephoneNo)
     VALUES 
         (10001, 'John Doe', '123 Elm St', '1112233445'),
         (10002, 'Jane Smith', '456 Pine St', '2223344556'),
         (10003, 'Mark Johnson', '789 Oak St', '3334455667'),
         (10004, 'Linda White', '101 Birch St', '4445566778'),
         (10005, 'Paul Brown', '202 Cedar St', '5556677889');
"""
cursor.execute(insertOwnerQuery)

#Show Clinic Data 
Clinic = pd.read_sql_query("SELECT * FROM Clinic", db_connect)
print(Clinic)
#Show Staff Data 
Staff = pd.read_sql_query("SELECT * FROM Staff", db_connect)
print(Staff)
#Show Examination Data 
Examination = pd.read_sql_query("SELECT * FROM Examination", db_connect)
print(Examination)
#Show Pet Data 
Pet = pd.read_sql_query("SELECT * FROM Pet", db_connect)
print(Pet)
#Show Owner Data 
Owner = pd.read_sql_query("SELECT * FROM Owner", db_connect)
print(Owner)
print("\n")

queryNumber1 = """
    SELECT s.*,c.cAddress
    FROM Staff s
    INNER JOIN Clinic c ON s.clinicNo = c.clinicNo
    WHERE c.cAddress ='123 Main St'
"""

queryNumber1 = pd.read_sql_query(queryNumber1, db_connect)
print(queryNumber1)


queryNumber2 = """
    SELECT strftime('%m', ex.dateSeen) AS month, COUNT(*) AS frequency
    FROM Examination ex
    INNER JOIN Staff s ON ex.staffNo = s.staffNo
    GROUP BY month
    ORDER BY frequency DESC
    LIMIT 1
"""

queryNumber2 = pd.read_sql_query(queryNumber2, db_connect)
print(queryNumber2)

queryNumber3 = """
    SELECT p.clinicNo,count(ex.examNo) AS numVisits
    FROM Examination ex
    INNER JOIN Pet p ON ex.petNo = p.petNo
    GROUP BY p.clinicNo
    ORDER BY COUNT(ex.examNo) DESC
    LIMIT 1;
"""

queryNumber3 = pd.read_sql_query(queryNumber3, db_connect)
print(queryNumber3)

queryNumber4 = """
    SELECT ex.staffNo,s.sName
    FROM Examination ex
    INNER JOIN Pet p ON ex.petNo = p.petNo
    INNER JOIN Staff s on ex.staffNo =s.staffNo
    WHERE p.pBreed = "Golden Retriever"
    
"""

queryNumber4 = pd.read_sql_query(queryNumber4, db_connect)
print(queryNumber4)

queryNumber5 = """
    SELECT o.*,c.cName
    FROM Owner o
    INNER JOIN Pet p ON o.ownerNo= p.ownerNo
    INNER JOIN Clinic c on p.clinicNo =c.clinicNo
"""
queryNumber5 = pd.read_sql_query(queryNumber5, db_connect)
print(queryNumber5)



# Commit any changes to the database
db_connect.commit()

# Close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
db_connect.close()

