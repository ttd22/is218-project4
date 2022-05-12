from app import db
from app.auth.forms import *
from flask_login import FlaskLoginClient
from app.db.models import User

def test_access_dashboard_accepted(application):
    application.test_client_class = FlaskLoginClient

    user = User('ttd22@njit.edu', 'testtest', True)
    db.session.add(user)
    db.session.commit()
    assert user.email == 'ttd22@njit.edu'
    assert db.session.query(User).count() == 1

    with application.test_client(user=user) as client:
        response = client.get('/dashboard')
        assert b'ttd22@njit.edu' in response.data
        assert response.status_code == 200


def test_access_dashboard_denied(application, client):
    application.test_client_class = FlaskLoginClient
    assert db.session.query(User).count() == 0
    with application.test_client(user = None) as client:
        # This request already has a user logged in.
        response = client.get('/dashboard')
        assert response.status_code == 302
