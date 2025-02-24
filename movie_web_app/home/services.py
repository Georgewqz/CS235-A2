from movie_web_app.adapters.repository import AbstractRepository
from movie_web_app.domainmodel.movie import User
from werkzeug.security import generate_password_hash, check_password_hash


class NameNotUniqueException(Exception):
    pass


class UnknownUserException(Exception):
    pass


class AuthenticationException(Exception):
    pass

class NonExistentArticleException(Exception):
    pass


def add_user(username: str, password: str, repo: AbstractRepository):
    # Check that the given username is available.
    user = repo.get_user(username)
    if user is not None:
        raise NameNotUniqueException

    # Encrypt password so that the database doesn't store passwords 'in the clear'.
    password_hash = generate_password_hash(password)

    # Create and store the new User, with password encrypted.
    user = User(username, password_hash)
    repo.add_user(user)


def get_user(username: str, repo: AbstractRepository):
    user = repo.get_user(username)
    if user is None:
        raise UnknownUserException

    return user_to_dict(user)


def authenticate_user(username: str, password: str, repo: AbstractRepository):
    authenticated = False

    user = repo.get_user(username)
    if user is not None:
        authenticated = check_password_hash(user.password, password)
    if not authenticated:
        raise AuthenticationException


# ===================================================
# Functions to convert model entities to dictionaries
# ===================================================

def user_to_dict(user):
    user_dict = {
        'username': user.username,
        'password': user.password
    }
    return user_dict


def get_movie_by_id(repo: AbstractRepository):
    id_list = repo.get_movie_by_id()
    return id_list


def get_movies(id_list, repo: AbstractRepository):
    movies = repo.get_movie(id_list)
    return movies
