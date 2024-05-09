# Import the dependencies
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from datetime import datetime, timedelta

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################

# Update the path to the SQLite database file
engine = create_engine("sqlite:///../Resources/hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/&lt;start&gt;<br/>"
        f"/api/v1.0/temp/&lt;start&gt;/&lt;end&gt;<br/>"
        )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return a JSON representation of precipitation data"""
    results = session.query(Measurement.date, Measurement.prcp).all()
    precipitation_data = {date: prcp for date, prcp in results}
    return jsonify(precipitation_data)

@app.route("/api/v1.0/stations")
def stations():
    """Return a JSON list of stations from the dataset"""
    results = session.query(Station.station).all()
    stations_data = [station for station, in results]
    return jsonify(stations_data)

@app.route("/api/v1.0/tobs")
def tobs():
    """Return a JSON list of Temperature Observations (tobs) for the previous year"""
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    last_year_date = dt.datetime.strptime(last_date, '%Y-%m-%d') - dt.timedelta(days=365)
    tobs_data = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date >= last_year_date).all()
    tobs_data_dict = {date: tobs for date, tobs in tobs_data}
    return jsonify(tobs_data_dict)

@app.route("/api/v1.0/temp/<start>")
def calc_temps(start):
    """When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date"""
    start_date = dt.datetime.strptime(start, "%Y-%m-%d")
    query_data = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
        filter(Measurement.date >= start_date).all()
    temps = list(np.ravel(query_data))
    return jsonify(temps)

@app.route("/api/v1.0/temp/<start>/<end>")
def calc_temps2(start, end):
    """When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive"""
    start_date = dt.datetime.strptime(start, "%Y-%m-%d")
    end_date = dt.datetime.strptime(end, "%Y-%m-%d")
    query_data = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
        filter(Measurement.date.between(start_date, end_date)).all()
    temps = list(np.ravel(query_data))
    return jsonify(temps)

if __name__ == "__main__":
    app.run(debug=False)
