from re import L, T
from typing import Type
from numpy import deprecate_with_doc
from pymysql import ROWID
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

# Flask-Bootstrap requires this line
# Bootstrap(app)

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
    rowid = db.Column(db.Integer, primary_key=True)
    Directory = db.Column(db.String)
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

    def __init__(self, rowid, Directory, LSD, SC, TWP, RG, W, M, adjusted_UWI, Latitude, Longitude, stress):
        self.rowid = rowid
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

class Properties(db.Model):
    __tablename__ = 'wellProperties'
    rowid = db.Column(db.Integer, primary_key=True)
    Directory = db.Column(db.String)
    Depth = db.Column(db.String)
    Type = db.Column(db.String)
    Description = db.Column(db.String)
    AdditionalNotes = db.Column(db.String)
    Shmin = db.Column(db.String)
    Shmax = db.Column(db.String)
    VerticalStress = db.Column(db.String)
    Temperature = db.Column(db.String)
    PorePressure = db.Column(db.String)
    YoungsModulus = db.Column(db.String)
    ShearModulus = db.Column(db.String)
    BulkModulus = db.Column(db.String)
    PoissonsRatio = db.Column(db.String)
    CohesiveStrength = db.Column(db.String)
    FrictionAngle = db.Column(db.String)
    pWave = db.Column(db.String)
    sWave = db.Column(db.String)

    def __init__(self, rowid, Directory, Depth, Type, Description, AdditionalNotes, Shmin, Shmax, VerticalStress, Temperature,
                PorePressure, YoungsModulus, ShearModulus, BulkModulus, PoissonsRatio, CohesiveStrength, FrictionAngle, pWave, sWave):
        self.rowid = rowid
        self.Directory = Directory
        self.Depth = Depth
        self.Type = Type
        self.Description = Description
        self.AdditionalNotes = AdditionalNotes
        self.Shmin = Shmin
        self.Shmax = Shmax
        self.VerticalStress = VerticalStress
        self.Temperature = Temperature
        self.PorePressure = PorePressure
        self.YoungsModulus = YoungsModulus
        self.ShearModulus = ShearModulus
        self.BulkModulus = BulkModulus
        self.PoissonsRatio = PoissonsRatio
        self.CohesiveStrength = CohesiveStrength
        self.FrictionAngle =FrictionAngle
        self.pWave = pWave
        self.sWave = sWave

    
@app.route('/select_record2/', methods=['POST'])
def select_record2():
    # alphabetical lists by sock name, chunked by letters between _ and _
    # .between() evaluates first letter of a string
    id = request.form['id']
    wells = Properties.query.filter(Properties.Directory == id).all()
    nameFilter = Properties.query.filter(Properties.Directory == id).first()
    name = nameFilter.Directory

    # depths = []
    # for well in wells:
    #     depth = well.split()[0]
    #     depth = int(depth)
    #     depths.append(depth)

    # depths.sort()

    #sort the entries in ascending depth
    return render_template('select_record2.html', wells=wells, name=name) 
