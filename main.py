import sqlite3
import os 
print(os.getcwd())


conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE)
''')

cursor.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)", ("Alice", 30, "alice@example.com"))

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.commit()
conn.close() 

# try:
#     # Code to create table
#     cursor.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)''')
# except sqlite3.Error as e:
#     print(f"An error occurred: {e}")