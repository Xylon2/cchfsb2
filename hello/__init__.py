import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World! This environment is "' \
        + os.environ['APP_ENV'] + '"</h1>'
