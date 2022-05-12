
import os
from app import db,auth
from app.db.models import User, Transactions
from app.auth.forms import csv_upload
from flask_login import FlaskLoginClient
from flask_login import login_user, login_required, logout_user, current_user
from app.auth.forms import login_form, register_form

def test_upload_csv(application):
    application.test_client_class = FlaskLoginClient
    user = User('ttd22@njit.edu', 'testtest', True)
    db.session.add(user)
    db.session.commit()
    assert user.email == 'ttd22@njit.edu'
    assert db.session.query(User).count() == 1


    with application.test_client(user = user) as client:
        # This request already has a user logged in.
        response = client.get('/transactions/upload')
        assert response.status_code == 200
        # form = csv_upload()
        # form.file = transactions_csv
        # assert form.validate

        root = os.path.dirname(os.path.abspath(__file__))
        transactions_csv = os.path.join(root, '../uploads/transactions.csv')
        transactions_csv_data = open(transactions_csv, 'rb')
        data = {'file': (transactions_csv_data,'transactions.csv')}

        response = client.get('/transactions/upload',data = data)
        assert response.status_code == 200
        # assert response.headers["Location"] == "/transactions"


# def test_update_csv_verification(test_client):
#     root = os.path.dirname(os.path.abspath(__file__))
#     transactions_csv = os.path.join(root, '../uploads/transactions.csv')
#     response = test_client.post('/songs/upload', data=transactions_csv)
#     assert response.status_code == 201

def test_upload_csv_denied(application,client):
    application.test_client_class = FlaskLoginClient
    assert db.session.query(User).count() == 0
    with application.test_client(user = None) as client:
        # This request already has a user logged in.
        response = client.get('/transactions/upload')
        assert response.status_code == 302

#
# def test_upload_csv_verification(application, client):
#     with application.test_request_context():
#     #     form = login_form()
#     #     form.email.data = "ttd22@njit.edu"
#     #     form.password.data = "trangdang"
#     #     form.submit
#     #     assert form.validate
#     #     user = User.query.filter_by(email=form.email.data).first()
#     #     if user is not None:
#     #         user.authenticated = True
#     #         db.session.add(user)
#     #         db.session.commit()
#     #         login_user(user)
#     #         flash("Welcome", 'success')
#         user = User('ttd22@njit.edu', 'testtest', True)
#         # user.authenticated = True
#         db.session.add(user)
#         db.session.commit()
#         login_user(user)
#         assert current_user.is_authenticated
#         response = client.get('/transactions/upload')
#         assert response.status_code == 200
#     # with application.test_client() as client:
#     #     # This request already has a user logged in.
#     #     response = client.get('/songs/upload')
#     #     assert response.status_code == 200
#
