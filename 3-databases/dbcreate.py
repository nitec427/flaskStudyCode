import os  # To access the absolute path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# We need to organize a directory for our database.
basedir = os.path.abspath(os.path.dirname(__file__))
# __file__ points to our file 

app = Flask(__name__)

# Configure the database url so that you can create
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

# By using the code below, we ignore every update and focus on the necessary ones.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

# After cretating the database, we need to use migrate
Migrate(app,db)
################# MODEL CREATION #############################
class Puppy(db.Model):
    # SQLAlchemy automatically takes the class name and make it plural according to grammatical rules but if we want to
    # we can name our database

    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for entries

    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.Text)
    
    
    def __init__(self, name, age,breed):
        self.name = name
        self.age = age
        self.breed = breed
    def __repr__(self):
        # String representation of the object
        return f"Puppy {self.name} is {self.age} years old. I am {self.breed}"
