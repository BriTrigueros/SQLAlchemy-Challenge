# SQLAlchemy Challenge

## Introduction
This project involves conducting a climate analysis about Honolulu, Hawaii, using Python, SQLAlchemy, and Flask. The analysis includes exploring a climate database, performing precipitation and station analyses, and designing a Flask API to present the results.

## Getting Started
1. Create a new repository for this project called sqlalchemy-challenge. Do not add this assignment to an existing repository.
2. Clone the new repository to your computer.
3. Inside your local Git repository, create a directory for this Challenge. Use a folder name that corresponds to the Challenge, such as SurfsUp.
4. Add your Jupyter notebook and app.py to this folder. They’ll contain the main scripts to run for analysis. Also add the Resources folder, which contains the data files you will be using for this challenge.
5. Push the changes to GitHub or GitLab.

## Files
Download the following files to help you get started:

[Module 10 Challenge files](#)

## Part 1: Analyze and Explore the Climate Data
In this section, you’ll use Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database.

### Precipitation Analysis
1. Find the most recent date in the dataset.
2. Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.
3. Load the query results into a Pandas DataFrame and sort the values by "date".
4. Plot the results and print the summary statistics for the precipitation data.

### Station Analysis
1. Design a query to calculate the total number of stations in the dataset.
2. Design a query to find the most-active stations and their observation counts.
3. Design a query to calculate the lowest, highest, and average temperatures for the most-active station.

## Part 2: Design Your Climate App
Now that you’ve completed your initial analysis, you’ll design a Flask API based on the queries that you just developed.

### Routes
- `/`: Start at the homepage and list all available routes.
- `/api/v1.0/precipitation`: Convert the query results from the precipitation analysis to a dictionary and return a JSON representation.
- `/api/v1.0/stations`: Return a JSON list of stations from the dataset.
- `/api/v1.0/tobs`: Query the dates and temperature observations of the most-active station for the previous year of data and return a JSON list of temperature observations.
- `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`: Return a JSON list of the minimum, average, and maximum temperature for a specified start or start-end range.

### Hints
- Join the station and measurement tables for some of the queries.
- Use the Flask `jsonify` function to convert your API data to a valid JSON response object.
