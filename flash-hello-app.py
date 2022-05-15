from re import S
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://oiyadi:oyinlola@localhost:5432/oiyadi'

db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'Hello World!'

