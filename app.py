import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

#saving references to tables
Measurement = Base.classes.measurement
Station = Base.classes.station

########################################################
#Flask Setup
########################################################
app = Flask(__name__)

##########################################################
#Flask route
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"<br/>"
        f"-list of Precipitation data in dictionary<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"<br/>"
        f"-list of Stations<br/>"        
        f"/api/v1.0/stations<br/>"
        f"<br/>"
        f"- List of prior year temperatures from most active station<br/>"
        f"/api/v1.0/tobs<br/>"
        f"<br/>"
        f"-The MIN/AVG/MAX temperature for all dates greater than and equal to given start date<br/>"
     
        f"/api/v1.0/date<br/>"
        
        f"<br/>"
        f"/api/v1.0/start/end<br/>"
        f"- The MIN/AVG/MAX temperature for dates between the start and end date inclusive<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    #create session link from python to the database
    session = Session(engine)
    """Return list of precipitation values along with corresponding dates."""
    #query the precipitaiton values with corresponding date
    prcp_results = session.query(Measurement.date,Measurement.prcp).order_by(Measurement.date.desc()).all()
    session.close()
    
    #creating dictionary for dates and precipitation values
    precipitation_values = []
    
    for date, prcp in prcp_results:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp
        precipitation_values.append(prcp_dict)
        
    return jsonify(precipitation_values)

#Defining route for station
@app.route("/api/v1.0/stations")
def stations():
    #create session link from python to the database
    session = Session(engine)
    """Return the list of stations"""
    #query the station names from the database
    stations = session.query(Station.station).all()
    
    #close the session
    session.close()
    #convert the tuples into normal list
    station_names = list(np.ravel(stations))
    return jsonify(station_names)
    
#defining route for prior year temperature for most active station
@app.route("/api/v1.0/tobs")
def temperature():
    #create session link from python to the database
    session = Session(engine)
    """Return the temperatture data"""
    #query the prior year temperature from the database
    temperature_results = session.query(Measurement.date, Measurement.tobs).\
             filter(Measurement.date >'2016-08-23').\
                order_by(Measurement.date).all()
    session.close()
    #creating dictionary for dates and temperature values
    temperature_values = []
    
    for date, tobs in temperature_results:
        temp_dict = {}
        temp_dict["date"] = date
        temp_dict["tobs"] = tobs
        temperature_values.append(temp_dict)
        
    return jsonify(temperature_values)

#defining the route for max, min and average temperature for a given start date

@app.route("/api/v1.0/<date>")
def temperature_startdate(date):
    session = Session(engine)
    temp_data = session.query(func.max(Measurement.tobs), func.min(Measurement.tobs),func.avg(Measurement.tobs)).\
               filter(Measurement.date >= date).all()
    session.close()
    temp = list(np.ravel(temp_data))
    
    return jsonify(temp)
    


#defining the route for max, min and average temperature for a given start date and end date

@app.route("/api/v1.0/<start>/<end>")
def temperature_startend(start,end):
    session = Session(engine)
    temp_startend = session.query(func.max(Measurement.tobs), func.min(Measurement.tobs),func.avg(Measurement.tobs)).\
               filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    session.close()
    temp_se = list(np.ravel(temp_startend))
    
    return jsonify(temp_se)
    



if __name__ == '__main__':
    app.run(debug=True)
  
    














