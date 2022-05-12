import logging

from app import db
from app.db.models import User, Transactions
from faker import Faker

def test_adding_user(application):
    log = logging.getLogger("myApp")
    with application.app_context():
        assert db.session.query(User).count() == 0
        #showing how to add a record
        #create a record
        user = User('ttd22@njit.edu', 'testtest',True)
        #add it to get ready to be committed
        db.session.add(user)
        #call the commit
        db.session.commit()
        #assert that we now have a new user
        assert db.session.query(User).count() == 1
        #finding one user record by email
        user = User.query.filter_by(email='ttd22@njit.edu').first()
        log.info(user)
        #asserting that the user retrieved is correct
        assert user.email == 'ttd22@njit.edu'
        # Adding user transactions
        user.transactions = [Transactions("200", "CREDIT"), Transactions("2000", "CREDIT")]
        db.session.commit()
        # transaction_count = db.session.query(Transactions).count()
        # assert db.session.query(Transactions).count() == transaction_count + 2

        # Checking transaction changes #1
        transaction1 = Transactions.query.filter_by(type='CREDIT').first()
        assert transaction1.type == "CREDIT"
        transaction1.amount = "200"
        db.session.commit()

        # Checking transaction changes #2
        transaction2 = Transactions.query.filter_by(amount='2000').first()
        assert transaction2.type == "CREDIT"

        # checking cascade delete
        db.session.delete(user)
        # assert db.session.query(User).count() == user_count
        # assert db.session.query(Transactions).count() == transaction_count



