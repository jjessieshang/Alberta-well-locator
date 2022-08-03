from re import L, T
from typing import Type
from numpy import deprecate_with_doc
from app import app
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy

from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, RadioField, HiddenField, StringField, IntegerField, FloatField
from wtforms.validators import DataRequired, InputRequired, Length, Regexp, NumberRange
from datetime import date

# the name of the database; add path if necessary
# db_name = 'ats.sqlite'
app.config['SECRET_KEY'] = 'BitCanGeosciences'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Users/jessieshang/Documents/summer_programming_projects/Alberta-Well-Locator/ats.sqlite'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy(app)

# each table in the database needs a class to be created for it
# db.Model is required - don't change it
# identify all columns by name and data type
class Coordinates(db.Model):
    __tablename__ = 'ATS'
    UWI = db.Column(db.String, primary_key=True)
    Latitude = db.Column(db.Float)
    Longitude = db.Column(db.Float)

class Directory(db.Model):
    __tablename__ = 'directory'
    Directory = db.Column(db.String, primary_key=True)
    LSD = db.Column(db.Float)
    SC = db.Column(db.Float)
    TWP = db.Column(db.Float)
    RG = db.Column(db.Float)
    W = db.Column(db.String)
    M = db.Column(db.Float)
    adjusted_UWI = db.Column(db.String)
    Latitude = db.Column(db.Float)
    Longitude = db.Column(db.Float)
    stress = db.Column(db.String)

    def __init__(self, Directory, LSD, SC, TWP, RG, W, M, adjusted_UWI, Latitude, Longitude, stress):
        self.Directory = Directory
        self.LSD = LSD
        self.SC = SC
        self.TWP = TWP
        self. RG = RG
        self.W = W
        self.M = M
        self.adjusted_UWI = adjusted_UWI
        self.Latitude = Latitude
        self.Longitude = Longitude

@app.route('/directory/')
def directory():
    uwi = Directory.query.order_by(Directory.Directory).all()
    return render_template('directory.html', uwi=uwi)

    # @app.route('/database/')
#     def read():
#         #Printing the data table
#         try:
#             uwi = Properties.query.all()
#             return render_template('database.html', uwi=uwi)
#         except Exception as e:
#             # e holds description of the error
#             error_text = "<p>The error:<br>" + str(e) + "</p>"
#             hed = '<h1>Something is broken.</h1>'
#     return hed + error_text