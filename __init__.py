from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(
    user='root', password='Rosberum2306', server='127.0.0.1', database='lab7')


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
engine = db.engine

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

SessionFactory = sessionmaker(bind=engine)

from Package import models, routs