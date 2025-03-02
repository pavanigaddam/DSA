import json
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('roster.sqlite')
cur = conn.cursor()

# Create tables with role column added to Member table
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;

CREATE TABLE User (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
);

CREATE TABLE Course (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT UNIQUE
);

CREATE TABLE Member (
    user_id INTEGER,
    course_id INTEGER,
    role INTEGER,
    PRIMARY KEY (user_id, course_id)
);
''')

# Load JSON data
fname = 'roster_data.json'
with open(fname, 'r') as f:
    data = json.load(f)

# Insert data into tables
for entry in data:
    name, title, role = entry

    # Insert or ignore User
    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (name,))
    cur.execute('SELECT id FROM User WHERE name = ?', (name,))
    user_id = cur.fetchone()[0]

    # Insert or ignore Course
    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (title,))
    cur.execute('SELECT id FROM Course WHERE title = ?', (title,))
    course_id = cur.fetchone()[0]

    # Insert Member with role
    cur.execute('INSERT OR REPLACE INTO Member (user_id, course_id, role) VALUES (?, ?, ?)', (user_id, course_id, role))

# Commit changes and close connection
conn.commit()

# Run the first query
print("First Query Result:")
cur.execute('''
SELECT User.name, Course.title, Member.role 
FROM User JOIN Member JOIN Course 
ON User.id = Member.user_id AND Member.course_id = Course.id
ORDER BY User.name DESC, Course.title DESC, Member.role DESC 
LIMIT 2;
''')
for row in cur.fetchall():
    print(row[0], "|", row[1], "|", row[2])

# Run the second query
print("\nSecond Query Result:")
cur.execute('''
SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X 
FROM User JOIN Member JOIN Course 
ON User.id = Member.user_id AND Member.course_id = Course.id
ORDER BY X LIMIT 1;
''')
print(cur.fetchone()[0])

# Close connection
cur.close()
