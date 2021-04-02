import os
import re
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import request
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
    response = '<h1>Hello World! This environment is "' \
        + os.environ['APP_ENV'] + '"</h1>'

    if request.method == 'POST':
        new_animal = Farm(animal=request.form['animal'], diet=request.form['diet'])
        db.session.add(new_animal)
        db.session.commit()

    response += '<p>The farm has these animals:</p><ul>'
    for entry in Farm.query:
        response += '<li>' + entry.animal + ' eats ' + entry.diet + '</li>'

    response += '</ul>'
    
    response += '''<form action="/" method="post"><br>
Animal: <input type="text" name="animal">
eats: <input type="text" name="diet">
<input type="submit" value="Submit">
</form>'''
    
    return response
