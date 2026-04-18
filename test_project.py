import sqlite3
import pytest
import project 

@pytest.fixture
def db_connection():
    # Create a fresh in-memory DB for each test
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
    
    project.conn = conn
    project.c = c
    yield conn
    conn.close()

def test_display_movies(db_connection, capfd):
    db_connection.execute("""
        INSERT INTO contents(name, year, genre, language, run_time, content_type, status, director, protagonist)
        VALUES ('Inception', 2010, 'Sci-Fi', 'English', 148, 'movie', 'completed', 'Nolan', 'DiCaprio')
    """)

    db_connection.commit()

    project.display_movies()
    captured = capfd.readouterr()
    assert "Inception (2010)" in captured.out
    assert "Sci-Fi" in captured.out

def test_display_series(db_connection, capfd):
    db_connection.execute("""
        INSERT INTO contents(name, year, genre, language, seasons, episodes, content_type, status, director, protagonist)
        VALUES ('Dark', 2017, 'Sci-Fi', 'German', 3, 26, 'series', 'completed', 'Baran bo Odar', 'Louis Hofmann')
    """)
    db_connection.commit()

    project.display_series()
    captured = capfd.readouterr()
    assert "Dark (2017)" in captured.out
    assert "Seasons: 3" in captured.out

def test_search_content(db_connection, capfd):
    db_connection.execute("""
        INSERT INTO contents(name, year, genre, language, run_time, content_type, status, director, protagonist)
        VALUES ('Interstellar', 2014, 'Sci-Fi', 'English', 169, 'movie', 'completed', 'Nolan', 'McConaughey')
    """)
    db_connection.commit()

   #testing search 
    def fake_input(prompt=""):
        return "Interstellar"
    project.input = fake_input

    project.search_content()
    captured = capfd.readouterr()
    assert "Movie found: Interstellar (2014)" in captured.out
    assert "Runtime: 169 min" in captured.out

