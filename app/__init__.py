"""A simple flask web app"""
import logging
import os

import flask_login
from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_cors import CORS
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect

from app.auth import auth
from app.cli import create_database, create_log_folder
from app.context_processors import utility_text_processors
from app.db import database
from app.db import db
from app.db.models import User
from app.error_handlers import error_handlers
from app.logging_config import log_con, LOGGING_CONFIG
from app.map import map
from app.simple_pages import simple_pages


mail = Mail()

login_manager = flask_login.LoginManager()

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    if app.config["ENV"] == "production":
        app.config.from_object("app.config.ProductionConfig")
    elif app.config["ENV"] == "development":
        app.config.from_object("app.config.DevelopmentConfig")
    elif app.config["ENV"] == "testing":
        app.config.from_object("app.config.TestingConfig")

    app.mail = Mail(app)
    # https://flask-login.readthedocs.io/en/latest/  <-login manager
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    csrf = CSRFProtect(app)
    bootstrap = Bootstrap5(app)

    # these load functions with web interface
    app.register_blueprint(simple_pages)
    app.register_blueprint(auth)
    app.register_blueprint(database)

    # these load functionality without a web interface
    app.register_blueprint(log_con)
    app.register_blueprint(error_handlers)

    # app.register_blueprint(songs)
    app.register_blueprint(map)
    app.context_processor(utility_text_processors)

    # add command function to cli commands
    app.cli.add_command(create_database)
    app.cli.add_command(create_log_folder)

    # app.add_url_rule("/", endpoint="index")
    db.init_app(app)
    api_v1_cors_config = {
        "methods": ["OPTIONS", "GET", "POST"],
    }
    CORS(app, resources={"/api/*": api_v1_cors_config})
    return app


@login_manager.user_loader
def user_loader(user_id):
    try:
        return User.query.get(int(user_id))
    except:
        return None
