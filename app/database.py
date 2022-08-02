from typing import Type
from numpy import deprecate_with_doc
from app import app
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# the name of the database; add path if necessary
# db_name = 'ats.sqlite'
app.config['SECRET_KEY'] = 'BitCanGeosciences'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Users/jessieshang/Documents/summer_programming_projects/Alberta-Well-Locator/ats.sqlite'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy(app)

# Flask-Bootstrap requires this line
Bootstrap(app)

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
    stress = db.Column(db.Float)

class Properties(db.Model):
    __tablename__ = 'wellProperties'
    Directory = db.Column(db.String, primary_key=True)
    Depth = db.Column(db.String)
    Type = db.Column(db.String)
    Description = db.Column(db.String)
    AdditionalNotes = db.Column(db.String)
    Minimumhorizontalstress = db.Column(db.String)
    Maximumhorizontalstress = db.Column(db.String)
    Verticalstress = db.Column(db.String)
    Temperature = db.Column(db.String)
    PorePressure = db.Column(db.String)
    Youngsmodulus = db.Column(db.String)
    ShearModulus = db.Column(db.String)
    BulkModulus = db.Column(db.String)
    Poissonsratio = db.Column(db.String)
    Cohesivestrength = db.Column(db.String)
    Frictionangle = db.Column(db.String)
    Pwave = db.Column(db.String)
    Swave = db.Column(db.String)

class ReadForm(FlaskForm):
    name = StringField('Which actor is your favorite?', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/database/')
def read():
    # try:
    #     uwi = Directory.query.all()
    #     uwi_text = '<ul>'
    #     for well in uwi:
    #         uwi_text += '<li>' + well.adjusted_UWI + ', ' + well.Directory + '</li>'
    #     uwi_text += '</ul>'
    #     return uwi_text
    # except Exception as e:
    #     # e holds description of the error
    #     error_text = "<p>The error:<br>" + str(e) + "</p>"
    #     hed = '<h1>Something is broken.</h1>'
    #     return hed + error_text
        # get a list of unique values in the style column
    try:
        uwi = Directory.query.all()
        return render_template('database.html', uwi=uwi)
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text
