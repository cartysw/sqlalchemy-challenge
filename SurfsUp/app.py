# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################

# Create engine using the `hawaii.sqlite` database file
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Declare a Base using `automap_base()`
Base = automap_base()

# Use the Base class to reflect the database tables
Base.prepare(autoload_with=engine)

# Assign the measurement class to a variable called `Measurement` and
# the station class to a variable called `Station`
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session
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
        f"To See Daily Precipitation Results from the Previous Year, Go Here: /api/v1.0/precipitation<br/>"
        f"To See a List of All the Stations in the Dataset, Go Here: /api/v1.0/stations<br/>"
        f"To See Stats for the Most Active Station from the Previous Year (ID: USC00519281), Go Here: /api/v1.0/tobs<br/>"
        f"The Next 2 Will Show The Minimum, Maximum, and Average Recorded Temperatures for your Specified Start (and End) Dates: <br/>"
        f"Specific Start Date Only: /api/v1.0/YYYY-MM-DD<br/>"
        f"Start Date and End Date Options: /api/v1.0/YYYY-MM-DD/YYYY-MM-DD<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Calculate and display precipitation totals from the previous year"""

    """Define year value and query for the data"""
    prev_Year = '2016-08-23'
    precip_Query = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_Year).\
        order_by(Measurement.date).all()
    
    """Create a dictionary from the gathered data"""
    precip_Values = []
    for date, prcp in precip_Query:
        precip_Dict = {}
        precip_Dict['Date'] = date
        precip_Dict['Precipitation'] = prcp
        precip_Values.append(precip_Dict)

    """Return a JSON version of the results"""
    return jsonify(precip_Values)

@app.route("/api/v1.0/stations")
def stations():
    """Return a JSON list of all the stations in the dataset"""

    """Query the stations table for the station IDs"""
    station_Info = session.query(Station.station, Station.name).all()

    """Create a list of the station IDs"""
    station_Values = list(np.ravel(station_Info))

    """Return a JSON version of the results"""
    return jsonify(station_Values)

@app.route("/api/v1.0/tobs")
def tobs():
    """Find the dates and temperature observations of the most active station for the previous year of data"""

    """Query the measurements table for the data"""
    prev_Year = '2016-08-23'
    active_Temps = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_Year).all()
    
    """Create a dictionary of the dates and temperatures"""
    """Additional Comment: Opted for a dictionary instead of a list because I'm querying for 2 things"""
    temp_Values = []
    for date, tobs in active_Temps:
        temp_Dict = {}
        temp_Dict['Date'] = date
        temp_Dict['Temperature'] = tobs
        temp_Values.append(temp_Dict)

    """Return a JSON version of the results"""
    return jsonify(temp_Values)

@app.route("/api/v1.0/<start>")
def specificstart(start):
    """Calculate the minimum, maximum, and average temperature for the specified start date to the end of the dataset"""

    """Query for results using the given start date"""
    start_Results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
        filter(Measurement.date >= start).all()
    
    """Create a dictionary for the min, max, and average temp results"""
    start_Values = []
    for min, max, avg in start_Results:
        start_Dict = {}
        start_Dict['Minimum Recorded Temperature'] = min
        start_Dict['Maximum Recorded Temperature'] = max
        start_Dict['Average Recorded Temperature'] = avg
        start_Values.append(start_Dict)

    """Return a JSON version of the results"""
    return jsonify(start_Values)

@app.route("/api/v1.0/<start>/<end>")
def specificstart_end(start, end):
    """Calculate the minimum, maximum, and average temperature for the specified start date to the specified end date"""

    """Query for results using the given start and end date"""
    end_Results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    
    """Create a dictionary for the min, max, and average temp results"""
    end_Values = []
    for min, max, avg in end_Results:
        end_Dict = {}
        end_Dict['Minimum Recorded Temperature'] = min
        end_Dict['Maximum Recorded Temperature'] = max
        end_Dict['Average Recorded Temperature'] = avg
        end_Values.append(end_Dict)

    """Return a JSON version of the results"""
    return jsonify(end_Values)

# End the Session
session.close()

if __name__ == '__main__':
    app.run(debug=True)