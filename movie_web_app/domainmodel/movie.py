from movie_web_app.domainmodel.director import Director
from movie_web_app.domainmodel.actor import Actor
from movie_web_app.domainmodel.genre import Genre


class Movie:
    def __init__(self, title: str, release_year: int):
        self.__director = None
        self.__description = None
        self.__actors = []
        self.__genres = []
        self.__runtime_minutes = None
        self.__id = None
        self.__last_actor = None

        if title != "":
            self.__title = title
        else:
            self.__title = None

        if release_year >= 1900:
            self.__release_year = release_year
        else:
            self.__release_year = None

    def __repr__(self):
        return f"<Movie {self.title}, {self.release_year}>"

    def __eq__(self, other):
        return self.title == other.title and self.release_year == other.release_year

    def __lt__(self, other):
        if self.__title == other.__title:
            return self.__release_year < other.__release_year
        else:
            return self.__title < other.__title

    def __hash__(self):
        return hash((self.title, self.release_year))

    @property
    def title(self) -> str:
        return self.__title

    @property
    def release_year(self) -> int:
        return self.__release_year

    @property
    def description(self) -> str:
        return self.__description

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def last_actor(self):
        return self.actors[-1]

    @property
    def last_genre(self):
        return self.genres[-1]

    @description.setter
    def description(self, new_description):
        self.__description = new_description

    @property
    def director(self) -> Director:
        return self.__director

    @director.setter
    def director(self, director: Director):
        self.__director = director

    @property
    def genres(self) -> list:
        return self.__genres

    @property
    def actors(self) -> list:
        return self.__actors

    @property
    def runtime_minutes(self) -> int:
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, runtime: int):
        if runtime <= 0:
            raise ValueError
        else:
            self.__runtime_minutes = runtime

    def add_actor(self, actor: Actor):
        self.__actors.append(actor)

    def remove_actor(self, actor: Actor):
        if actor in self.__actors:
            self.__actors.remove(actor)

    def add_genre(self, genre: Genre):
        self.__genres.append(genre)

    def remove_genre(self, genre: Genre):
        if genre in self.__genres:
            self.__genres.remove(genre)


class User:
    def __init__(self, username: str, password: str):
        self._username: str = username
        self._password: str = password
        self._comments: List[Comment] = list()

    @property
    def username(self) -> str:
        return self._username

    @property
    def password(self) -> str:
        return self._password

    @property
    def comments(self):
        return iter(self._comments)

    def add_comment(self, comment: 'Comment'):
        self._comments.append(comment)

    def __repr__(self) -> str:
        return f'<User {self._username} {self._password}>'

    def __eq__(self, other) -> bool:
        if not isinstance(other, User):
            return False
        return other._username == self._username



