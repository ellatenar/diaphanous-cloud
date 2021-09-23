from flask import Flask
from os import environ
from flask_pymongo import PyMongo

app = Flask(__name__)

mongoURI = environ.get("MONGO_URI")

# mongodb_client = PyMongo(app, mongoURI)
# db = mongodb_client.db

import diaphanous.views