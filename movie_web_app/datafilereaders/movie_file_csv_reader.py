import csv

from movie_web_app.domainmodel.movie import Movie
from movie_web_app.domainmodel.actor import Actor
from movie_web_app.domainmodel.genre import Genre
from movie_web_app.domainmodel.director import Director


class MovieFileCSVReader:
    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__dataset_of_directors = []
        self.__dataset_of_actors = []
        self.__dataset_of_movies = []
        self.__dataset_of_genres = []

    def read_csv_file(self):
        with open('/Users/georgewang/Desktop/CS235-A2-main/movie_web_app/datafiles/movies.csv', mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            for row in movie_file_reader:
                title = row['Title']
                release_year = int(row['Year'])
                director = Director(row['Director'])
                movie = Movie(title, release_year)
                movie.id = row['Rank']
                movie.description = row['Description']
                movie.director = director
                movie.runtime_minutes = int(row['Runtime (Minutes)'])

                for actor in row['Actors'].split(","):
                    movie.add_actor(Actor(actor))

                for genre in row['Genre'].split(","):
                    movie.add_genre(Genre(genre))

                self.__dataset_of_movies.append(movie)

                if director not in self.__dataset_of_directors:
                    self.dataset_of_directors.append(director)

                for actor in row['Actors'].split(","):
                    if Actor(actor) not in self.__dataset_of_actors:
                        self.dataset_of_actors.append(Actor(actor))

                for genre in row['Genre'].split(","):
                    if Genre(genre) not in self.__dataset_of_genres:
                        self.dataset_of_genres.append(Genre(genre))

    @property
    def dataset_of_actors(self):
        return self.__dataset_of_actors

    @property
    def dataset_of_directors(self):
        return self.__dataset_of_directors

    @property
    def dataset_of_movies(self):
        return self.__dataset_of_movies

    @property
    def dataset_of_genres(self):
        return self.__dataset_of_genres
