import datetime as dt
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
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
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/station"
    )

'''
@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return a list of precipitation"""
    # Query all precipitation and dates
    results = session.query(Measurement.date,Measurement.prcp).all()

    # Convert list of tuples into normal list
    all_results = list(np.ravel(results))

    # Create a dictionary from the row data and append to a list of all_passengers
    all_precip = []
    for result in all_results:
        precip_dict = {}
        precip_dict["date"] = Measurement.date
        precip_dict["prcp"] = Measurement.prcp
        all_precip.append(precip_dict)

    return jsonify(all_precip)
'''
@app.route("/api/v1.0/station")
def station():
    """Return a list of stations"""
    # Query all stations
    results = session.query(Measurement.station).all()

    # Convert list of tuples into normal list
    all_results = list(np.ravel(results))

    return jsonify(all_results)

@app.route("/api/v1.0/tobs")
def tobs():
    """return a list of tobs and dates from one year ago"""
    #query all tobs
    results = session.query(Measurement.date,Measurement.tobs).all()

    #last data point
    lastdate = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    
    #calculate year ago
    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=366)

    #query yearago datat
    yearago_results=session.query(Measurement.date,Measurement.tobs).\
        filter(Measurement.date == query_date).all()

    return jsonify(yearago_results)
"""
@app.route("/api/v1.0/start")
@app.route("/api/v1.0/startend")
"""
if __name__ == '__main__':
    app.run(debug=True)
