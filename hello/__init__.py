import os
import re
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = re.sub('postgres://', 'postgresql://', os.environ['DATABASE_URL'])

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Farm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    animal = db.Column(db.String(128))
    diet = db.Column(db.String(128))

@app.route('/')
def index():
    return '<h1>Hello World! This environment is "' \
        + os.environ['APP_ENV'] + '"</h1>'
