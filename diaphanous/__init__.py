from flask_pymongo import PyMongo
from flask import Flask
from os import environ

app = Flask(__name__)

mongoURI = environ.get("MONGO_URI")

mongodb_client = PyMongo(app, uri=mongoURI)

import diaphanous.views