import sqlite3

# 1. Connect to database
connection = sqlite3.connect("school.db")

# 2. Create cursor
cursor = connection.cursor()

# 3. Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

# 4. Insert data
cursor.execute(
    "INSERT INTO students (name, age) VALUES (?, ?)",
    ("Rahul", 20),
)


connection.commit()

# 5. Read data
cursor.execute("SELECT * FROM students")
 
students = cursor.fetchall()

for student in students:
    print(student)

# 6. Close connection
connection.close()