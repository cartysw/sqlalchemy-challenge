Hello!

This is a repository for the SQL Alchemy challenge for the UofM Data Analytics Bootcamp course.

This project was focused on a dataset concerning recorded weather data from Hawaii. We had to create an Exploratory Data Analysis script and a Flask API app based on it.

The objectives for the Exploratory Data Analysis script were to:
  - Set up an engine, declare a base, reflect the data tables, assign the tables to classes, and start a session
  - Find the most recent date in the data set
  - Create a query to retrieve precipitation data from the most recent 12 months, save the results to a dataframe, and plot the dataframe using Matplotlib
  - Use Pandas to calculate a summary statistics table for the precipitation data
  - Calculate the total number of weather stations using a query
  - Create a query to find the most active stations and list their counts in descending order
  - Find the lowest, highest, and average temperature recorded from the most active weather station
  - Create a query to gather data from the most recent 12 months from the most active weather station, and plot the results as a histogram

For the Flask API app we were tasked with:
  - Creating a homepage route
  - Creating a route that converts the query results from the precipitation analysis to a dictionary format and returning that as a JSON
  - Creating a route that returns a list of the weather stations from the dataset in JSON format
  - Creating a route that queries the dates and temperatures observations of the most active station for the previous year and returns that in JSON format
  - Create a dynamic route that takes a start date input and returns a list of the minimum, maximum, and average temperatures from that date to the most recent date. Also, return that list in JSON format
  - Create a final route that also allows you to enter an end date to gather temperature data in a specific range. Same as before, return the resulting list in JSON format


 The routes for the app and their descriptions are as follows:
  - To See Daily Precipitation Results from the Previous Year, Go Here: /api/v1.0/precipitation
  - To See a List of All the Stations in the Dataset, Go Here: /api/v1.0/stations
  - To See Stats for the Most Active Station from the Previous Year (ID: USC00519281), Go Here: /api/v1.0/tobs
  - Specific Start Date Only: /api/v1.0/YYYY-MM-DD
  - Start Date and End Date Options: /api/v1.0/YYYY-MM-DD/YYYY-MM-DD<end>

Instructions for running the program:
  - Download the project files
  - For the Data Analysis, open the climate_starter file in Jupyter Notebook (the program used to write the script) and run the cells at your discretion
  - For the Flask API App, run the program in Git Bash and either follow the homepage instructions for finding route info or refer to the descriptions above

Here are the references I used during the development of this project:
Referenced code from here to write function that finds date 1 year before the most recent date in dataset:
https://stackoverflow.com/questions/5158160/python-get-datetime-for-3-years-ago-today

Had trouble with my precipitation bar graph showing each individual date on the x-axis. I referenced this to change it from rain_Df.plot.bar() to rain_Df.plot():
https://stackoverflow.com/questions/57677559/differences-between-bar-plots-in-matplotlib-and-pandas

Referenced pandas .describe function documentation for writing summary statistics table code:
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html

Used code from here to create function that find the most active station in the Measurement table:
https://stackoverflow.com/questions/62676385/sqlalchemy-query-to-count-the-times-that-a-value-exist-in-a-column

Got help from XPert Learning Assistant with modifying the active station query to make it output results in descending order:
how do i modify this to output the results in descending order? session.query(Measurement.station, func.count(Measurement.station)).\ group_by(Measurement.station).all()

Referenced this page for building query to calculate some specific summary statistics for the most active station:
https://www.geeksforgeeks.org/sqlalchemy-core-functions/
