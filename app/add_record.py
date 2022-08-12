from re import L, T
import re
from typing import Type
from numpy import deprecate_with_doc
from app import app
import pandas as pd
import numpy as np
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
import sqlite3

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
        self.stress = stress

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
    Directory = StringField('Well Location (e.g. CVE-12-18-100-3W4)', [ InputRequired()])

    # updated - date - handled in the route function
    updated = HiddenField()
    submit = SubmitField('Add/Update Record')

@app.route('/add_record', methods=['GET', 'POST'])
def add_record():
    conn = sqlite3.connect('ats.sqlite')
    ATS = pd.read_sql_query("SELECT * FROM ats", con=conn)
    conn.close()

    #sectional ATS numpy matrix
    arr = np.arange(1,37)
    arr = np.sort(arr)[::-1]
    arr = arr.reshape(6,6)
    df = pd.DataFrame(arr)
    df.iloc[0::2,:] = df.iloc[0::2,::-1]

    array = df.to_numpy()

    def lsdToQuarter(UWI):
        """ Associate the legal subdivision to the adjacent quarter section corner. If position 
            is bottom left, print the section.
        """
        
        # sort subdivision
        lsd = UWI[4]

        if (lsd == 2 or lsd == 3 or lsd == 6):
            UWI[4] = 'S4'
        elif (lsd == 10 or lsd == 11 or lsd == 13 or lsd == 14 or lsd == 15):
            UWI[4] = 'N4'
        elif (lsd == 1 or lsd == 7 or lsd == 8 or lsd == 9):
            UWI[4] = 'E4'
        elif (lsd == 4 or lsd == 5 or lsd == 12):
            UWI[4] = 'W4'
        elif (lsd == 16):
            UWI[4] = 'NE'
            
        #sort section
        sc = UWI[4]
        
        if (sc == 'S4'):
            result = np.where(array == UWI[3])
        elif (sc == 'W4'):
            result = np.where(array == UWI[3])
        else:
            result = 100
            
        return UWI, result

    def new_coordinate(coord, UWI_):
        """ a function to rename the section of a location based input index applied to matrix of 36 sections
        """
        tp = UWI_[4]
        if coord == 100:
            y1 = 100
            x1 = 100
            
        else:
            x1 = int(coord[0])
            y1 = int(coord[1])
        
            if tp == 'S4':
                if x1 == 5:
                    tp = 'E4'
                else:
                    x1 += 1
                    tp = 'N4'

        
            elif tp == 'W4':
                if y1 == 0:
                    tp = 'N4'
            
                else:
                    y1 = y1 - 1
                    tp = 'E4'
        
        UWI_[4] = tp
        x = x1
        y = y1
        
        return UWI_, x, y

    def ListToString(list_form):
        """ A function to convert from list to string
        """
        median = str(list_form[0])

        range_str = str(list_form[1])
        UWIrg = range_str.zfill(2)
        
        township_str = str(list_form[2])
        township = township_str.zfill(3)
        
        section_str = str(list_form[3])
        section = section_str.zfill(2)
        
        qs = str(list_form[4])
        
        wellID = median + UWIrg + township + section + qs
        
        return(wellID)

    form1 = AddRecord()
    if form1.validate_on_submit():
        directory = request.form['Directory']

        #processing the entered string
        input_uwi = directory

        input_UWI = input_uwi.split('-')

        LSD = float(input_UWI[1])
        sc = float(input_UWI[2])
        twp = float(input_UWI[3])

        last = re.split("w", input_UWI[4], flags=re.IGNORECASE)
        rg = float(last[0])
        M = float(last[1])
        W ="W"
        stress = "0 N"

        UWI_number = [int(M),int(rg),int(twp),int(sc),int(LSD)]

        # #MAIN TERMINAL CODE...more uwi manipulation
        UWI_list = UWI_number
        UWI, co = lsdToQuarter(UWI_list)
        UWI, x, y = new_coordinate(co, UWI)

        # call on the matrix and output the number at that index, assign as new section
        if x == 100:
            pass

        else:
            new_sc = array[x,y]
            UWI[3] = new_sc
            
        UWI_ID = ListToString(UWI)

        input_coord = ATS.loc[ATS['UWI'] == UWI_ID]
        lati1 = float(input_coord.iloc[0]['Latitude'])
        long1 = float(input_coord.iloc[0]['Longitude'])

        # the data to be inserted into Sock model - the table, socks
        record = Directory(directory, LSD, sc, twp, rg, W, M, UWI_ID, lati1, long1, stress)
        # # Flask-SQLAlchemy magic adds record to database
        db.session.add(record)
        db.session.commit()
        # # create a message to send to the template
        message = f"The data for well {directory} has been submitted."
        return render_template('add_record.html', message=message)
    else:
        for field, errors in form1.errors.items():
            for error in errors:
                flash("Error in {}: {}".format(
                    getattr(form1, field).label.text,
                    error
                ), 'error')
        return render_template('add_record.html', form1=form1)
