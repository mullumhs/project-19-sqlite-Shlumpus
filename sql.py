import sqlite3

conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

# Select all movies

cursor.execute('SELECT * FROM movies')
all_movies = cursor.fetchall()
print("All movies:")
for movie in all_movies:
    print(movie)

cursor.execute('''
UPDATE movies
SET rating = 9.0
WHERE title = 'Inception'
''')

# Create the movies table
cursor.execute('''
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    director TEXT,
    year INTEGER,
    rating FLOAT
)
''')
conn.commit()

movie = ('', 'Francis Ford Coppola', 1972, 9.2)

cursor.execute(f'''
INSERT INTO movies (title, director, year, rating)
VALUES ('{movie[0]}', '{movie[1]}', {movie[2]}, {movie[3]})
''')
conn.commit()
conn.close()
