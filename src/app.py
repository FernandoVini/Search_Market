from flask import Flask, jsonify
from flask_restx import Api, Resource, reqparse, fields
from flask_sqlalchemy import SQLAlchemy
import pathlib
import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + str(pathlib.Path(__file__).parent.resolve()) + '/supermarkets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

api = Api(app)
db = SQLAlchemy(app)

parser = reqparse.RequestParser()
parser.add_argument('name', help="Supermarket's name")


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


# MODEL OF SUPERMARKET REGISTRY
supermarket_model = api.model(
    'Supermarket',
    {
        'id': fields.Integer(),
        'name': fields.String(),
        'site': fields.String(),
        'data_management': fields.DateTime()
    }
)


@api.route('/supermarkets/')
class Supermarkets(Resource):
    """
    Api who covers the supermarket's management
    """
    @api.marshal_list_with(supermarket_model, code=200, envelope='supermarkets')
    def get(self):
        supermarkets = Supermarket.query.all()
        return supermarkets

    def post(self):
        ...


@api.route('/supermarket/<int:page_id>')
class SupermarketResource(Resource):
    """
    Get supermarket by ID
    """

    @api.marshal_with(supermarket_model, code=200, envelope='supermarket')
    def get(self, page_id):
        supermarket = Supermarket.query.get_or_404(page_id)
        return supermarket

    def post(self):
        ...
    def delete(self):
        ...


@app.shell_context_processor
def shell_context():
    """
    Sending commands by shell with 'flask shell' command
    :return:
    """
    return {
        'db': db,
        'Supermarket': Supermarket
    }


if __name__ == '__main__':
    app.run(debug=True)


