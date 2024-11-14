import sqlite3

movies = [
    ('', 'Francis Ford Coppola', 1972, 9.2),
    ('Travels of Glombulous McStumpulinkian', 'Stinken Bink', 1562, 10)
    ('Ice Women Diary, A Witchs Tin Key', 'Dondary Stompenhagen', 1912, 8.4)
    ('Donkus The Impeccable Failure', 'Stoopy Doopy The Twentieth', 2024, 0)
]

def create_connection():
    conn = sqlite3.connect('my_movie_collection.db')
    return conn

def create_table(conn):
    cursor = conn.cursor()
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


def add_movie(conn, title, director, year, rating):
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO movies(title, director, year, rating)
    VALUES ('{title}', '{director}', '{year}', '{rating}')
    ''')
    conn.commit()

def display_all_movies(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM movies')
    all_movies = cursor.fetchall()
    #all movies message
    print("All movies:")

    #actually printing all the movies
    for movie in all_movies:
    print(movie)
    conn.commit

def update_movie_rating(conn, title, movie_rating):
    #UPDATING A MOVIE
    cursor = conn.cursor()
    cursor.execute(f'''
    UPDATE movies
    SET rating = {movie_rating}
    WHERE title = '{title}'
    ''')
    conn.commit

def delete_movie(conn, title)
    cursor = conn.cursor()
    cursor.execute(f'''
    DELETE FROM movies WHERE title = '{title}'
    ''') 
    conn.commit

def main():

    conn = create_connection()

    if conn is not None:

        create_table(conn)

        

        while True:

            print("\n--- Movie Database Manager ---")

            print("1. Add a new movie")

            print("2. Display all movies")

            print("3. Update a movie's rating")

            print("4. Delete a movie")

            print("5. Find movies by director")

            print("6. Exit")

            

            choice = input("Enter your choice (1-6): ")

            

            if choice == '1':

                title = input("Enter movie title: ")

                director = input("Enter director name: ")

                year = int(input("Enter release year: "))

                rating = float(input("Enter rating (0-10): "))

                add_movie(conn, title, director, year, rating)

                print("Movie added successfully!")

            

            elif choice == '2':

                display_all_movies(conn)

            

            elif choice == '3':

                title = input("Enter movie title to update: ")

                new_rating = float(input("Enter new rating (0-10): "))

                update_movie_rating(conn, title, new_rating)

                print("Rating updated successfully!")

            

            elif choice == '4':

                title = input("Enter movie title to delete: ")

                delete_movie(conn, title)

                print("Movie deleted successfully!")

            

            elif choice == '5':

                director = input("Enter director name: ")

                find_movies_by_director(conn, director)

            

            elif choice == '6':

                print("Thank you for using Movie Database Manager. Goodbye!")

                break

            

            else:

                print("Invalid choice. Please try again.")

        

        conn.close()

    else:

        print("Error! Cannot create the database connection.")



if __name__ == '__main__':

    main()