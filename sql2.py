import csv
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('tracks.sqlite')
cur = conn.cursor()

# Drop tables if they exist
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
''')

# Create the tables
cur.executescript('''
CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

# Read the CSV file and insert data into the database
with open('tracks.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')  # Use comma as the delimiter
    for row in reader:
        # Skip rows that don't have exactly 7 columns
        if len(row) != 7:
            print(f"Skipping malformed row: {row}")
            continue

        # Extract data from the row
        try:
            track_title = row[0]    # Index 0: Track Title
            artist_name = row[1]    # Index 1: Artist Name
            album_title = row[2]    # Index 2: Album Title
            track_length = int(row[3]) if row[3] else 0  # Index 3: Track Length (handle empty values)
            track_rating = int(row[4]) if row[4] else 0  # Index 4: Track Rating (handle empty values)
            track_count = int(row[5]) if row[5] else 0   # Index 5: Play Count (handle empty values)
            genre_name = row[6]     # Index 6: Genre Name
        except (IndexError, ValueError) as e:
            print(f"Error extracting data from row: {row}. Error: {e}")
            continue

        # Insert Artist
        cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist_name,))
        cur.execute('SELECT id FROM Artist WHERE name = ?', (artist_name,))
        artist_id = cur.fetchone()[0]

        # Insert Genre
        cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (genre_name,))
        cur.execute('SELECT id FROM Genre WHERE name = ?', (genre_name,))
        genre_id = cur.fetchone()[0]

        # Insert Album
        cur.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)', (album_title, artist_id))
        cur.execute('SELECT id FROM Album WHERE title = ?', (album_title,))
        album_id = cur.fetchone()[0]

        # Insert Track
        cur.execute('INSERT OR IGNORE INTO Track (title, album_id, genre_id, len, rating, count) VALUES (?, ?, ?, ?, ?, ?)',
                    (track_title, album_id, genre_id, track_length, track_rating, track_count))

# Commit the changes and close the connection
conn.commit()
conn.close()