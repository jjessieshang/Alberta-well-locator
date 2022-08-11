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

class AddProperty(FlaskForm):
    # id used only by update/edit
    id_field = HiddenField()
    Directory = HiddenField()
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

class DeleteForm(FlaskForm):
    id_field = HiddenField()
    purpose = HiddenField()
    submit = SubmitField('Delete This Record')

def stringdate():
    today = date.today()
    date_list = str(today).split('-')
    # build string in format 01-01-2000
    date_string = date_list[1] + "-" + date_list[2] + "-" + date_list[0]
    return date_string
    
# result of edit - this function updates the record
@app.route('/edit_result', methods=['POST'])
def edit_result():
    id = request.form['id_field']
    # call up the record from the database
    well = Properties.query.filter(Properties.rowid == id).first()
    # update all values
    well.Directory = request.form['Directory']
    well.Depth = request.form['Depth']
    well.Type = request.form['Type']
    well.Description = request.form['Description']
    well.AdditionalNotes = request.form['AdditionalNotes']
    well.Shmin = request.form['Shmin']
    well.Shmax = request.form['Shmax']
    well.VerticalStress = request.form['VerticalStress']
    well.Temperature = request.form['Temperature']
    well.PorePressure = request.form['PorePressure']
    well.YoungsModulus = request.form['YoungsModulus']
    well.ShearModulus = request.form['ShearModulus']
    well.BulkModulus = request.form['BulkModulus']
    well.PoissonsRatio = request.form['PoissonsRatio']
    well.CohesiveStrength = request.form['CohesiveStrength']
    well.FrictionAngle = request.form['FrictionAngle']
    well.pWave = request.form['pWave']
    well.sWave = request.form['sWave']

    # get today's date from function, above all the routes
    well.updated = stringdate()

    form1 = AddProperty()
    if form1.validate_on_submit():
        # update database record
        db.session.commit()
        # create a message to send to the template
        message = f"The data for well {well.Directory} has been updated."
        return render_template('result.html', message=message)
    else:
        # show validaton errors
        well.rowid = id
        # see https://pythonprogramming.net/flash-flask-tutorial/
        for field, errors in form1.errors.items():
            for error in errors:
                flash("Error in {}: {}".format(
                    getattr(form1, field).label.text,
                    error
                ), 'error')
        return render_template('edit_or_delete.html', form1=form1, well=well, choice='edit')