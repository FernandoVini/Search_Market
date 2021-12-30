from src import app, api, db
from flask_restx import Api, Resource, reqparse, fields
from flask import request
from src.model.model import Supermarket, User

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

user_model = api.model(
    'User',
    {
        'id': fields.Integer(),
        'username': fields.String(),
        'password': fields.String(),
        'date_registered': fields.DateTime(),
        'isAdmin': fields.Boolean()
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
    @api.expect(supermarket_model)
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


@api.route('/users/')
class Clients(Resource):
    """
    An API to users management
    """
    @api.marshal_with(user_model, code=201, envelope='client')
    def get(self):
        """
        A method to get all system's users
        :return:
        """
        users = User.query.all()
        return users

    @api.marshal_with(user_model, code=201, envelope='client')
    @api.expect(user_model)
    def post(self):
        """
        Post method to get new user's information
        :return:
        """
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        isAdmin = data.get('isAdmin')

        new_user = User(username, password, isAdmin)

        db.session.add(new_user)
        db.session.commit()


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

    @api.marshal_with(supermarket_model, code=200, envelope='supermarket')
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
        'Supermarket': Supermarket,
        'User': User
    }


