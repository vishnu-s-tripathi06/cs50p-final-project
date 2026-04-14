class Catalogue:
    def __init__(self,catalogue_name):
        self.movies=[]
        self.series=[]
        self.catalogue_name=catalogue_name
    def add_movie(self,Movie):
        self.movies.append(Movie)
    def add_series(self,Series):
        self.series.append(Series)
    def list_movies(self):
        result=[]
        for m in self.movies:
            result.append(f"{m.name} : {m.year}")
        return result
    def list_series(self):
        result=[]
        for s in self.series:
            result.append(f"{s.name} : {s.year}")
        return result

class Content:
    def __init__(self,name,year,language,status,genre,director=None,protagonist=None):
        self.name=name
        self.year=year
        self.director=director
        self.protagonist=protagonist
        self.language=language
        self.genre=genre
        self.status=status

class Series(Content):
    def __init__(self,name,year,language,status,genre,seasons,episodes,director=None,protagonist=None,):
        super().__init__(
            name=name,
            year=year,
            director=director,
            protagonist=protagonist,
            language=language,
            status=status,
            genre=genre  )
        self.seasons=seasons
        self.episodes=episodes

    

    
class Movie(Content):
    def __init__(self,name,year,language,status,genre,run_time,director=None,protagonist=None):
        super().__init__(
            name=name,
            year=year,
            director=director,
            protagonist=protagonist,
            language=language,
            status=status,
            genre=genre
        )
        self.run_time=run_time
    

        




