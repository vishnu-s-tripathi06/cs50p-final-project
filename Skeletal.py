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

    

    pass
class Movies(Content):
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
    pass