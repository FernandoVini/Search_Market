from src import app
import pathlib

print(str(pathlib.Path(__file__).parent.resolve()))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + str(pathlib.Path(__file__).parent.resolve()) + '/src/supermarkets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True