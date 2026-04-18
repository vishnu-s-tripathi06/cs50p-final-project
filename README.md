# 🎬 Movie Catalogue (CS50 Final Project)

This is a personal Movie catalogue system where users can store the movies they have watched / watching/ plan to watch , users can enter all the information about the movie to store it in a sqlite3 database . 

We watch a Hundreds of movies but can't even name 5 when someone asks to recommend them a few. and especially in the case of Anime we forget who was the director , writter , number of episodes and number of seasons. 

Demo Video link: 

This is the structure of my CS50P project.
project/
│
├── project.py # Main CLI application
├── skeletal.py # OOP classes (Movie, Series, Catalogue)
├── test_project.py # Pytest test cases
├── Catalogue.DB # SQLite database (auto-generated)
├── requirements.txt # Project dependencies
└── README.md # Documentation
## ⚙️ Features of This project
All the funtions of this project are stored in `project.py` folder which also has all the sqlite3 quaries .The Movie Catalogue provides the following functionalities :

### 🎥 Content Management
- Add movies and TV series with detailed metadata
- Store information such as:
  - Name
  - Year of release
  - Language
  - Genre
  - Status (watched, watching, plan to watch)
  - Director and protagonist
  - Runtime (for movies)
  - Seasons and episodes (for series)

### 🔍 Search Functionality
- Search content by name
- Case-insensitive matching by converting everything to lowercase
- Displays complete details of matching entries
> [!WARNING]
>Type the exact name of the series or Movie which you want to search.

### 📋 Display Options
- View all movies in the database
- View all TV series separately
- View complete catalogue in a structured format

### 💾 Persistent Storage
- All data is stored in a SQLite database (`Catalogue.DB`)
- Data persists between program runs
- data can also be stored in ram using (":memory:") in place of (`Catalogue.DB`) if you want to test the functionality.

### 🧪 Testing Support
- Automated tests written using Pytest
- Ensures correctness of core functionalities

All these functionalities are basic but I aim to expand them in the web version. 

## 🧠 Object-Oriented Design

The project follows a structured Object oriented programming approach by having a separate `skeletal.py` file which contains all my classes namely Catalogue, Content , Movie and Series. 

### Base Class: Content
The `Content` class stores shared attributes such as name, year, genre, language, and status. It acts as the foundation for all media types.

### Derived Classes:
- **Movie** → Extends Content and adds runtime because that is how I measure movie duration .This inherits other parameters from the `Content` class.
- **Series** → Extends Content and adds seasons and episodes because some series have same name and can only be distinguished by number of seasons . having this also helps to track the watch history.

### Catalogue Class
The `Catalogue` class manages an in-memory collection of content objects. It is designed for future scalability, allowing features such as filtering, sorting, and analytics to be added easily. This feature will be used in the future when I make my program a android app or a web application as this is my personal project also. 

>[!Note] 
>Catalogue may seem redundant now or totally useless to have but in the future when I expland the funtanality of this program to launch it for global public it will be instrumental. 


## 🗄️ Database Design

The project uses SQLite for data persistence. The database contains a single table for storing all the different parameters . This is a personal database so I didn't think relational database would be necessary.

### contents

| Column       | Type    | Description                    |
|--------------|---------|--------------------------------|
| id           | INTEGER | Primary key                    |
| name         | TEXT    | Title of content               |
| year         | INTEGER | Release year                   |
| language     | TEXT    | Language of content            |
| status       | TEXT    | Watching status                |
| genre        | TEXT    | Genre of content               |
| run_time     | INTEGER | Movie runtime (if applicable)  |
| seasons      | INTEGER | Number of seasons (series)     |
| episodes     | INTEGER | Total episodes (series)        |
| content_type | TEXT    | Movie or Series                |
| director     | TEXT    | Director name                  |
| protagonist  | TEXT    | Main actor/character           |

### Reqirements
-pytest
-sqlite3 (it already comes installed with python but I am still mentioning it as you have to import it.)

## 🚀 How to Run the Project

### 1. Install dependencies

Before running the project make sure you have all required packages installed. Run the following command in your terminal:

```bash
pip install -r requirements.txt

### 2. Run the application by typing this in the terminal

python project.py

