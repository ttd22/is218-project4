import logging

from app import db
from app.db.models import User, Transactions
from app.auth.forms import *

# def test_csv_update(application, client):
#     csv = "uploads/music.csv"
#     # data = {
#     #     'csv': (open(csv), csv)
#     # }
#     file = open('uploads/music.csv')
#     response = client.post('/songs/upload',data = )
#     assert response.status_code == 201


# def test_csv_update(client):
#     """
#     Test that page one is up and returns a file after processing post requests.
#     """
#
#     # Convert csv file to bytes then send in the format the form expects
#     csv = "uploads/music.csv"
#     csv_data = open(csv, "rb")
#     data = {"file": (csv_data, "uploads/music.csv")}
#
#     response = client.post(
#         '/songs/upload',
#         data=data,
#         # buffered=True,
#         # content_type="multipart/form-data",
#     )
#
#     print(response)
#     assert response.status_code == 201
#     # assert response.status_code == 201

# def test_csv_verification(client):
#     form = csv_upload()
#     form.file = "uploads/music.csv"
#     assert form.validate()

# def test_file_upload():
#     client = app.test_client() # you will need your flask app to create the test_client
#     data = {
#         'file': (BytesIO('my file contents'), 'uploads/music.csv'), # we use StringIO to simulate file object
#     }
#     # note in that in the previous line you can use 'file' or whatever you want.
#     # flask client checks for the tuple (<FileObject>, <String>)
#     res = client.post('/songs/upload', data=data)
#     assert res.status_code == 200