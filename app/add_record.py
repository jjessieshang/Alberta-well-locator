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

class Properties(db.Model):
    __tablename__ = 'wellProperties'
    Directory = db.Column(db.String, primary_key=True)
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

    def __init__(self, Directory, Depth, Type, Description, AdditionalNotes, Shmin, Shmax, VerticalStress, Temperature,
                PorePressure, YoungsModulus, ShearModulus, BulkModulus, PoissonsRatio, CohesiveStrength, FrictionAngle, pWave, sWave):
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

class AddRecord(FlaskForm):
    # id used only by update/edit
    id_field = HiddenField()
    Directory = StringField('Well Name', [ InputRequired()])
    Depth = StringField('Depth')
    Type = StringField('Rock Type')
    Description = StringField('Description')
    AdditionalNotes = StringField('Notes')
    Shmin = StringField('Minimum horizontal stress')
    Shmax = StringField('Maximum horizontal stress')
    VerticalStress = StringField('Vertical stress')
    Temperature = StringField('Temperature')
    PorePressure = StringField('Pore Pressure')
    YoungsModulus = StringField('Young\'s Modulus')
    ShearModulus = StringField('Shear Modulus')
    BulkModulus = StringField('Bulk Modulus')
    PoissonsRatio = StringField('Poisson\'s ratio')
    CohesiveStrength = StringField('Cohesive Strength')
    FrictionAngle = StringField('Friction Angle')
    pWave = StringField('p Wave')
    sWave = StringField('s Wave')

    # updated - date - handled in the route function
    updated = HiddenField()
    submit = SubmitField('Add/Update Record')

@app.route('/add_record', methods=['GET', 'POST'])
def add_record():
    form1 = AddRecord()
    if form1.validate_on_submit():
        Directory = request.form['Directory']
        Depth = request.form['Depth']
        Type = request.form['Type']
        Description = request.form['Description']
        AdditionalNotes = request.form['AdditionalNotes']
        Shmin = request.form['Shmin']
        Shmax = request.form['Shmax']
        VerticalStress = request.form['VerticalStress']
        Temperature = request.form['Temperature']
        PorePressure = request.form['PorePressure']
        YoungsModulus = request.form['YoungsModulus']
        ShearModulus = request.form['ShearModulus']
        BulkModulus = request.form['BulkModulus']
        PoissonsRatio = request.form['PoissonsRatio']
        CohesiveStrength = request.form['CohesiveStrength']
        FrictionAngle = request.form['FrictionAngle']
        pWave = request.form['pWave']
        sWave = request.form['sWave']

        # the data to be inserted into Sock model - the table, socks
        record = Properties(Directory, Depth, Type, Description, AdditionalNotes, Shmin, Shmax, VerticalStress, Temperature,
                PorePressure, YoungsModulus, ShearModulus, BulkModulus, PoissonsRatio, CohesiveStrength, FrictionAngle, pWave, sWave)
        # Flask-SQLAlchemy magic adds record to database
        db.session.add(record)
        db.session.commit()
        # create a message to send to the template
        message = f"The data for well {Directory} has been submitted."
        return render_template('add_record.html', message=message)
    else:
        for field, errors in form1.errors.items():
            for error in errors:
                flash("Error in {}: {}".format(
                    getattr(form1, field).label.text,
                    error
                ), 'error')
        return render_template('add_record.html', form1=form1)

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