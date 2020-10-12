from flask import Flask
import os

from flask import Flask
import movie_web_app.adapters.repository as repo
from movie_web_app.adapters.memory_repository import MemoryRepository, populate


def create_app():

    app = Flask(__name__)

    app.config.from_object('config.Config')

    repo.repo_instance = MemoryRepository()
    populate('movie_web_app/datafiles/movies.csv', repo.repo_instance)
    populate('movie_web_app/datafiles/users.csv', repo.repo_instance)
    with app.app_context():
        # Register blueprints.
        from .home import home
        app.register_blueprint(home.home_blueprint)

    return app
