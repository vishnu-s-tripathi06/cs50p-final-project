import sqlite3
import project  # your main file name


# -----------------------------
# helper: create fresh DB
# -----------------------------
def setup_db():
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()

    c.execute("""
        CREATE TABLE contents(
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
    return conn, c


# -----------------------------
# TEST 1: insert movie (logic only)
# -----------------------------
def test_movie_insert():
    conn, c = setup_db()

    project.conn = conn
    project.c = c

    c.execute("""
        INSERT INTO contents
        (name, year, language, status, genre,
         run_time, seasons, episodes, content_type, director, protagonist)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        "Inception", 2010, "English", "completed", "Sci-Fi",
        148, None, None, "movie", "Nolan", "Leonardo"
    ))

    conn.commit()

    c.execute("SELECT name FROM contents WHERE name = 'Inception'")
    result = c.fetchone()

    assert result[0] == "Inception"


# -----------------------------
# TEST 2: insert series
# -----------------------------
def test_series_insert():
    conn, c = setup_db()

    project.conn = conn
    project.c = c

    c.execute("""
        INSERT INTO contents
        (name, year, language, status, genre,
         run_time, seasons, episodes, content_type, director, protagonist)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        "Dark", 2017, "German", "completed", "Thriller",
        None, 3, 26, "series", "Baran", "Jonas"
    ))

    conn.commit()

    c.execute("SELECT content_type FROM contents WHERE name = 'Dark'")
    result = c.fetchone()

    assert result[0] == "series"


# -----------------------------
# TEST 3: check empty DB
# -----------------------------
def test_empty_db():
    conn, c = setup_db()

    c.execute("SELECT * FROM contents")
    result = c.fetchall()

    assert result == []