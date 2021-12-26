from flask import Flask, jsonify, request
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
        """
        Getting all saved supermarkets
        :return: All supermarkets saved objects
        """
        supermarkets = Supermarket.query.all()
        return supermarkets

    @api.marshal_with(supermarket_model, code=201, envelope='supermarket')
    def post(self):
        """
        Post method to save new supermarket's information
        :return: Supermarket object
        """
        data = request.get_json()
        name = data.get('name')
        site = data.get('site')

        new_supermarket = Supermarket(name=name, site=site)

        db.session.add(new_supermarket)
        db.session.commit()

        return new_supermarket


@api.route('/supermarket/<int:obj_id>')
class SupermarketResource(Resource):
    """
    Get supermarket by ID
    """

    @api.marshal_with(supermarket_model, code=200, envelope='supermarket')
    def get(self, obj_id):
        """
        Getting a specific supermarket by ID
        :param obj_id: supermarket's ID
        :return: Supermarket's object, HTTP Code
        """
        supermarket = Supermarket.query.get_or_404(obj_id)
        return supermarket, 200

    @api.marshal_with(supermarket_model, envelope='supermarket')
    def put(self, obj_id):
        """
        Updating the existing supermarket's information
        :param obj_id: supermarket's ID
        :return: Supermarket's object, HTTP Code
        """
        on_update = Supermarket.query.get_or_404(obj_id)

        data = request.get_json()
        on_update.name = data.get('name')
        on_update.site = data.get('site')

        db.session.commit()

        return on_update, 200

    @api.marshal_with(supermarket_model, envelope='supermarket')
    def delete(self, obj_id):
        """
        This function will delete a supermarket from database
        :param obj_id: Supermarket's ID
        :return: Supermarket's object, HTTP Code
        """
        to_delete = Supermarket.query.get_or_404(obj_id)
        db.session.delete(to_delete)

        db.session.commit()

        return to_delete, 200


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


