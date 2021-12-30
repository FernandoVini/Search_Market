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


class User(db.Model):
    """
    Class who represents the website's administrators
    """

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(60), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    isAdmin = db.Column(db.Boolean(), nullable=False)
    date_registered = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, username, password, isAdmin):
        self.username = username
        self.password = password
        self.isAdmin = isAdmin

    def __repr__(self):
        return self.name

