import csv
import os
from bisect import bisect, bisect_left, insort_left
from datetime import date, datetime
from typing import List
from werkzeug.security import generate_password_hash
from movie_web_app.domainmodel.movie import Movie, User
from movie_web_app.adapters.repository import AbstractRepository
from movie_web_app.datafilereaders.movie_file_csv_reader import MovieFileCSVReader


class MemoryRepository(AbstractRepository):
    def __init__(self):
        self.__movies = []
        self.__movie_index = {}
        self._users = list()

    def add_user(self, user: User):
        self._users.append(user)

    def get_user(self, username) -> User:
        return next((user for user in self._users if user.username == username), None)

    def add_movie(self, movie: Movie):
        insort_left(self.__movies, movie)
        self.__movie_index[movie.id] = movie

    def get_movie(self, id_list):
        return [self.__movie_index[id] for id in id_list]

    def get_movie_by_id(self):
        return [i for i in self.__movie_index.keys()]


def load_users(data_path: str, repo: MemoryRepository):
    users = dict()

    for data_row in read_csv_file(os.path.join(data_path, 'users.csv')):
        user = User(
            username=data_row[1],
            password=generate_password_hash(data_row[2])
        )
        repo.add_user(user)
        users[data_row[0]] = user
    return users


def read_csv_file(filename: str):
    with open('movie_web_app/datafiles/users.csv', encoding='utf-8-sig') as infile:
        reader = csv.reader(infile)

        # Read first line of the the CSV file.
        headers = next(reader)

        # Read remaining rows from the CSV file.
        for row in reader:
            # Strip any leading/trailing white space from data read.
            row = [item.strip() for item in row]
            yield row


def populate(filename, repo: MemoryRepository):
    users = load_users(filename, repo)
    c = MovieFileCSVReader(filename)
    c.read_csv_file()
    for movie in c.dataset_of_movies:
        repo.add_movie(movie)
