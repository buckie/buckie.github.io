from flask import Flask
from flask_flatpages import FlatPages
from flask_frozen import Freezer

app = Flask(__name__)
app.config.from_pyfile('config.py')
pages = FlatPages(app)
freezer = Freezer(app)

from app import views
