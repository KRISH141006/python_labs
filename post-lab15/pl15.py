import sqlite3

# Connection or making a library
# db = sqlite3.connect('ms-lab/dbfiles/database.db')

#connecting from memory
db = sqlite3.connect("D:/d_drive/sem_3/pwp/ms-lab/dbfiles/database.db")

#creating a cursor object
cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS student_records(
                enrollment INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                subject1 TEXT NOT NULL,
                marks1 TEXT NOT NULL,
                subject2 TEXT NOT NULL,
                marks2 TEXT NOT NULL,
                subject3 TEXT NOT NULL,
                marks3 TEXT NOT NULL
)''')

#commiting the changes
db.commit()

student_records = [
    (92400133189,'Darshit Kacha','ED',94,'cad',92,'dld',90),
    (92400133108,'Krish Sondagar','ED',95,'cad',33,'dld',80),
    (92400133109,'Prince Vaghasiya','ED',96,'cad',99,'dld',98),
    (92400133154,'Akshat Shah','ED',97,'cad',100,'dld',90),
    (92400133191,'Taksh Amrutiya','ED',98,'cad',33,'dld',100),
]

#inserting the data
cursor.executemany('''INSERT INTO student_records (enrollment, name , subject1, marks1, subject2, marks2, subject3, marks3) 
                      VALUES (?, ? , ?, ?, ?, ?, ?, ?)''',student_records)

db.commit()


