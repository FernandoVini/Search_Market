from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api, Resource, reqparse, fields
from flask import request


app = Flask(__name__)
app.config.from_object('config')

api = Api(app, title='Supermarket API', description='An API to manage a Scraping application to our partners')
db = SQLAlchemy(app)

from .routes import routes


if __name__ == "__main__":
    app.run(debug=True)
