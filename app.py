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
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
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

if __name__ == '__main__':
    app.run(debug=True)
  
    














