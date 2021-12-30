import datetime
from src import db


class Supermarket(db.Model):
    """
    A class model who represents the supermarkets
    """
    id = db.Column(db.Integer(), primary_key=True)  # Creating a column with the supermarket's id
    name = db.Column(db.String(40), nullable=False)  # Creating a column with the supermarket's name
    site = db.Column(db.String(80), nullable=False)  # Creating a column with the supermarket's site
    data_management = db.Column(db.DateTime(), default=datetime.datetime.utcnow)

    def __repr__(self):
        return self.name