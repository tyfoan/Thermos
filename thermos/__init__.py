import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = b"hNk)\xd0u\x95\x7fl\xf2\xa6\xbe\x03\xec\xcc'\xc9\x07\xc2,\x05\x0e\xef("
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'thermos.db')
app.config['DEBUG'] = True
db = SQLAlchemy(app)

from . import models
from . import views
