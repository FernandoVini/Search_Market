from flask import Flask, jsonify
from flask_restx import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
import pathlib

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + str(pathlib.Path(__file__).parent.resolve()) + '/supermarkets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
db = SQLAlchemy(app)

parser = reqparse.RequestParser()
parser.add_argument('name', help="Supermarket's name")


@api.route('/supermarket/')
class Supermarket(Resource):
    def get(self):
        return jsonify({"Message": "Hello World"})
    def post(self):
        ...


@api.route('/supermarket/<int:id>')
class SupermarketResource(Resource):
    def get(self, id):
        ...
    def post(self):
        ...
    def delete(self):
        ...


if __name__ == '__main__':
    app.run(debug=True)


