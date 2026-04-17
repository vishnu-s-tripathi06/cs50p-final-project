class Catalogue:
    def __init__(self,catalogue_name):
    
        self.contents=[]
        self.catalogue_name=catalogue_name
  
    def add_content(self,content):
        self.contents.append(content)
    def display_collection(self):
        result=[]
        for _ in self.contents:
            result.append(_)
        return result
    

class Content:
    def __init__(self,name,year,language,status,genre,content_type,director=None,protagonist=None):
        self.name=name
        self.year=year
        self.director=director
        self.protagonist=protagonist
        self.language=language
        self.genre=genre
        self.content_type=content_type
        self.status=status


    def __str__(self):
        return f"{self.content_type.capitalize()}: {self.name} ({self.year}) - {self.genre}, {self.language}, Status: {self.status}"


class Series(Content):
    def __init__(self,name,year,language,status,genre,seasons,episodes,director=None,protagonist=None,):
        super().__init__(
            name=name,
            year=year,
            director=director,
            protagonist=protagonist,
            language=language,
            status=status,
            genre=genre ,
            content_type='series')
        self.seasons=seasons
        self.episodes=episodes
    
    def __str__(self):
        return (f"Series: {self.name} ({self.year}) - {self.genre}, {self.language}, "
                f"Seasons: {self.seasons}, Episodes: {self.episodes}, Status: {self.status}")

class Movie(Content):
    def __init__(self, name, year, language, status, genre, run_time, director=None, protagonist=None):
        super().__init__(
            name=name,
            year=year,
            language=language,
            status=status,
            genre=genre,
            content_type="movie", 
            director=director,
            protagonist=protagonist
        )
        self.run_time = run_time
    def __str__(self):
        return (f"Movie: {self.name} ({self.year}) - {self.genre}, {self.language}, "
                f"Runtime: {self.run_time} min, Status: {self.status}")






