import os
import re
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import request
from flask import render_template
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = re.sub('postgres://', 'postgresql://', os.environ['DATABASE_URL'])

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Farm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    animal = db.Column(db.String(128))
    diet = db.Column(db.String(128))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_animal = Farm(animal=request.form['animal'], diet=request.form['diet'])
        db.session.add(new_animal)
        db.session.commit()

    response = render_template('index.html',
                               environment=os.environ['APP_ENV'],
                               animals=Farm.query
    )
        
    return response
