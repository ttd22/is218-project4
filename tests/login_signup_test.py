import logging
from app import db
from app.db.models import User
from app.auth.forms import login_form, register_form
from faker import Faker
from flask_login import login_user, login_required, logout_user, current_user
from wtforms import Form as WTForm
from flask_wtf import Form as FlaskForm
from app.auth import login
from flask_login import current_user
from flask_login import FlaskLoginClient
from tests import conftest
from app import create_app, User


def test_user_login(application):
    log = logging.getLogger("myApp")
    log.info("user login test")
    with application.test_request_context():
        form = login_form()
        form.email.data = "ttd22@njit.edu"
        form.password.data = "testtest"
        form.submit
        assert form.validate

        # Another way to test
        user = User('ttd22@njit.edu', 'testtest', True)
        # user.authenticated = True
        db.session.add(user)
        db.session.commit()
        login_user(user)
        assert current_user.is_authenticated



def test_user_register(application):
    log = logging.getLogger("myApp")
    log.info("user register test")
    with application.test_request_context():
        form = register_form()
        form.email.data = "ttd22@njit.edu"
        form.password.data = "trangdang"
        form.confirm.data = "trangdang"
        form.submit
        assert form.validate

