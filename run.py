from src import app


# MODEL OF SUPERMARKET REGISTRY
"""supermarket_model = api.model(
    'Supermarket',
    {
        'id': fields.Integer(),
        'name': fields.String(),
        'site': fields.String(),
        'data_management': fields.DateTime()
    }
)"""


app.run(debug=True)


