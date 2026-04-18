import sqlite3
from Skeletal import Catalogue, Movie, Series
conn=sqlite3.connect("Catalogue.DB")#for tempory testing while coding database
c=conn.cursor()
c.execute("""
    CREATE TABLE IF NOT EXISTS contents(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              year INTEGER,
              language TEXT,
              status TEXT,
              genre TEXT,
              run_time INTEGER,
              seasons INTEGER,
              episodes INTEGER,
              content_type TEXT,
              director TEXT,
              protagonist TEXT
              )
""")
conn.commit()
catalogue = Catalogue("My Personal Movie Collection")
def main():
    Option=0
    while Option!=7:
        print("Your personal content catalogue")
        print("1. Add Movie")
        print("2. Add Series")
        print("3. Display the list of movies.")
        print("4. Display the list of Series.")
        print("5. Display the Entire Collection.")
        print("6. Serch content by name.")
        print("7. Exit")
        while True:
            try:
                Option=int(input("Enter a choice by typing the option number: ").strip())
                if Option>0 and Option<=7:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Enter an Integer value between 1-7.")
            
        

        match Option:
            case 1:
                add_content("movie")
            case 2:
                add_content("series")
            case 3:
                display_movies()
            case 4:
                display_series()
            case 5:
                display_content()
            case 6:
                search_content()
            case 7:
                return 0
conn.commit()

def add_content(content_type):
    name = input("Enter name: ").strip()
    while True:
        try:
            year = int(input("Enter release year: ").strip())
            break
        except:
            print("Enter year in numbers like xxxx.")
    language = input("Enter language: ").strip()
    status = input("Enter status (completed/watching/plan_to_watch): ").strip()
    genre = input("Enter genre: ").strip()
    director = input("Enter director: ").strip()
    protagonist = input("Enter protagonist: ").strip()

    # Createing object accouding to content_type feild in skeletal file
    if content_type == "movie":
        while True:
            try:
                run_time = int(input("Enter run time: ").strip())
                break
            except ValueError:
                print("Enter a valid number.")
        content = Movie(name, year, language, status, genre, run_time, director, protagonist)
        catalogue.add_content(content)
        seasons = None
        episodes = None


    else:  # series
        while True:
            try:
                seasons = int(input("Enter number of seasons: ").strip())
                break
            except ValueError:
                print("Enter a valid number.")

        while True:
            try:
                episodes = int(input("Enter total episodes: ").strip())
                break
            except:
                print("Enter a Valid number.")
        content = Series(name, year, language, status, genre, seasons, episodes, director, protagonist)
        catalogue.add_content(content)
        run_time = None

    # Insert into database
    c.execute("""
        INSERT INTO contents(
            name, year, language, status, genre,
            run_time, seasons, episodes,
            content_type, director, protagonist
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        content.name,
        content.year,
        content.language,
        content.status,
        content.genre,
        run_time,
        seasons,
        episodes,
        content.content_type,
        content.director,
        content.protagonist
    ))
    conn.commit()
    print(f"{content_type.capitalize()} '{content.name}' added successfully!")

def search_content():
    name = input("Enter the name of the content to search: ").strip().lower()
    c.execute("SELECT * FROM contents WHERE LOWER(name) = LOWER(?)", (name,))
    result = c.fetchone()
    if result:
        # Unpacking the row for readability
        (id, name, year, language, status, genre, run_time,
         seasons, episodes, content_type, director, protagonist) = result

        if content_type == "movie":
            print(f"Movie found: {name} ({year}) - {genre}, {language}, Runtime: {run_time} min, Status: {status}")
        elif content_type == "series":
            print(f"Series found: {name} ({year}) - {genre}, {language}, Seasons: {seasons}, Episodes: {episodes}, Status: {status}")
        else:
            print(f"{content_type.capitalize()} found: {name} ({year}) - {genre}, {language}, Status: {status}")
    else:
        print("Content not found.")


def display_movies():
        print("Here are your movies:")
        c.execute("SELECT name, year, genre, language, run_time FROM contents WHERE content_type='movie'")
        movies = c.fetchall()
        for m in movies:
            print(f"{m[0]} ({m[1]}) - {m[2]}, {m[3]}, Runtime: {m[4]} min")


def display_series():
    print("Here are your series:")
    c.execute("SELECT name, year, genre, language, seasons, episodes FROM contents WHERE content_type='series'")
    series = c.fetchall()
    for s in series:
        print(f"{s[0]} ({s[1]}) - {s[2]}, {s[3]}, Seasons: {s[4]}, Episodes: {s[5]}")


def display_content():
    print("\nHere is your entire content library:")
    print("=" * 70)
    c.execute("SELECT name, year, genre, language, content_type, status, run_time, seasons, episodes FROM contents")
    rows = c.fetchall()
    for row in rows:
        name, year, genre, language, content_type, status, run_time, seasons, episodes = row
        if content_type == "movie":
            print(f"Movie: {name} ({year}) - {genre}, {language}, Runtime: {run_time} min, Status: {status}")
        elif content_type == "series":
            print(f"Series: {name} ({year}) - {genre}, {language}, Seasons: {seasons}, Episodes: {episodes}, Status: {status}")
        else:
            print(f"{content_type.capitalize()}: {name} ({year}) - {genre}, {language}, Status: {status}")
        print("-" * 60)

if __name__=="__main__":
    main()
    








    






        

