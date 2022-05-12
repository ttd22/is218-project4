"""This makes the test configuration setup"""
# pylint: disable=redefined-outer-name
import os
import logging
from flask import current_app
import pytest
from app import create_app, User
from app.db import db


@pytest.fixture()
def application():
    """This makes the app"""
    #you need this one if you want to see whats in the database
    #os.environ['FLASK_ENV'] = 'development'
    #you need to run it in testing to pass on github
    os.environ['FLASK_ENV'] = 'testing'

    application = create_app()

    with application.app_context():
        db.create_all()
        yield application
        db.session.remove()
        #drops the database tables after the test runs
        db.drop_all()
    # return application

@pytest.fixture()
def add_user(application):
    with application.app_context():
        #new record
        user = User('ttd22@njit.edu', 'testtest', True)
        db.session.add(user)
        db.session.commit()

@pytest.fixture()
def client(application):
    """This makes the http client"""
    return application.test_client()



@pytest.fixture()
def runner(application):
    """This makes the task runner"""
    return application.test_cli_runner()

# @pytest.fixture()
# def test_client(application):
#     testing_client = application.test_client()
#     ctx = application.app_context()
#     ctx.push()
#     yield testing_client
#     ctx.pop()

