from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app:Flask = Flask(__name__)
app.config.from_pyfile('settings.cfg')
db:SQLAlchemy = SQLAlchemy(app)

# The Order is neccesary, otherwise no table will be created.
from .models import User
from .models import Tag
from .models import Todo

db.drop_all()
db.create_all()

from .controllers import *

