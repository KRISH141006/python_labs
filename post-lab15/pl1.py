import sqlite3

conn = sqlite3.connect("student_record.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS student (
                    enrollment INTEGER PRIMARY KEY,
                    name TEXT NOT NULL
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS subject (
                    subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    subject_name TEXT NOT NULL
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS enrollment (
                    enrollment INTEGER,
                    subject_id INTEGER,
                    mark INTEGER NOT NULL
                )''')

conn.commit()

subjects = ["PWP", "DS", "OOP", "Maths"]

for s in subjects:
    cursor.execute("INSERT INTO subject (subject_name) VALUES (?)", (s,))
conn.commit()

students = [
    (92301733016, "PRINCE VAGHASIYA"),
    (92301733017, "AKSHAT SHAH"),
    (92301733027, "TAKSH AMRUTIYA"),
    (92301733046, "HEET NATHVANTI"),
    (92301733058, "DARSHIT KACHA")
]

cursor.executemany("INSERT INTO student (enrollment, name) VALUES (?, ?)", students)
conn.commit()

subject_ids = cursor.execute("SELECT subject_id, subject_name FROM subject").fetchall()
sub_map = {name: sid for sid, name in subject_ids}

multi_enroll = [
    (92301733016, sub_map["PWP"], 95),
    (92301733016, sub_map["Maths"], 88),

    (92301733017, sub_map["PWP"], 85),
    (92301733017, sub_map["DS"], 79),

    (92301733027, sub_map["OOP"], 90),
    (92301733027, sub_map["DS"], 82),

    (92301733046, sub_map["PWP"], 93),
    (92301733046, sub_map["OOP"], 87),

    (92301733058, sub_map["PWP"], 75),
    (92301733058, sub_map["Maths"], 69)
]

cursor.executemany("INSERT INTO enrollment (enrollment, subject_id, mark) VALUES (?, ?, ?)", multi_enroll)
conn.commit()

rows = cursor.execute('''
    SELECT student.enrollment, student.name, subject.subject_name, enrollment.mark
    FROM enrollment
    JOIN student ON enrollment.enrollment = student.enrollment
    JOIN subject ON subject.subject_id = enrollment.subject_id
''').fetchall()

print("\nAll Student Enrollments:")
for r in rows:
    print(r)

high_marks = cursor.execute('''
    SELECT student.name, subject.subject_name, enrollment.mark
    FROM enrollment
    JOIN student ON enrollment.enrollment = student.enrollment
    JOIN subject ON subject.subject_id = enrollment.subject_id
    WHERE enrollment.mark > 90
''').fetchall()

print("\nStudents with marks > 90:")
for h in high_marks:
    print(h)

cursor.execute('''
    UPDATE enrollment SET mark = 98 
    WHERE enrollment = 92301733016 AND subject_id = ?
''', (sub_map["PWP"],))

conn.commit()

updated = cursor.execute('''
    SELECT student.name, subject.subject_name, mark 
    FROM enrollment
    JOIN student ON enrollment.enrollment = student.enrollment
    JOIN subject ON subject.subject_id = enrollment.subject_id
    WHERE student.enrollment = 92301733016 AND subject.subject_name = "PWP"
''').fetchone()

print("\nUpdated Record:", updated)

cursor.execute("DELETE FROM student WHERE name = 'DARSHIT KACHA'")
cursor.execute("DELETE FROM enrollment WHERE enrollment = 92301733058")
conn.commit()

print("\nDeleted DARSHIT KACHA successfully")

avg_mark = cursor.execute("SELECT AVG(mark) FROM enrollment").fetchone()[0]
print(f"\nAverage mark of all subjects: {avg_mark:.2f}")

conn.close()
