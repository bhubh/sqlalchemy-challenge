# sqlalchemy-challenge
In the first part of this project, SQL database is reflected into SQLalchemy ORM and SQLalchemy session queries are applied to retrieve, filter and analyze the database. The database has two tables: measurement and station, which hold information about different climate data recorded at different weather-stations. The precipitation data for last one year of the data has been filtered and plotted as Bar plot.

![Precipitation](https://user-images.githubusercontent.com/99154332/168450967-4ce436db-8736-46d2-b110-277d3bd67fd0.png)

Similarly histogram was plotted for temperature variation for last one year at most active weather-station. The plot shown as below: 

![Temperature](https://user-images.githubusercontent.com/99154332/168450991-5c2c90f3-e292-49e3-8083-8572aad42d1a.png)

<br>
# app.py
<br/>
In the second part of this project, selected data the database has been jsonified and uploaded into the wave address using app.route() function. 
<br/>
The precipitation data with corresponding date can be accessed from the following link: 
http://127.0.0.1:5000/api/v1.0/precipitation
