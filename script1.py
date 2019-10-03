'''
# Assignment title: Final Project- Script 1
# Web-scraping Weather Forecast Update
# Date: 10/02/2019
# Created by Team 2
# Description: The script web-scrapes the weather.gov website to extract the 5-Day weather forecast for a given location
# Reads Inputs: Latitude & Longitude in Decimal Degrees
# Outputs: 5-Day Weather Forecast
'''

# import required libraries
import requests
from bs4 import BeautifulSoup

# List to store response
forecast = []

## Ask for latitude and longitude for desired location 
##to check the forecast for
## Lat/lon in decimal degrees provided for Worcester, MA
##lat = '42.2634'
##lon = '-71.8022'
lat=str(input('Enter latitude of desired location: ')) # lat is accepted as string
lon=str(input('Enter longitude of desired location: ')) # lon is accepted as string

# Create url for the requested location through string concatenation
url = 'https://forecast.weather.gov/MapClick.php?lat='+lat+"&lon="+lon

# Check if the URL exists
print url

# Send request to retrieve the web-page using the get() function from the requests library
# The page variable stores the response from the web-page
page = requests.get(url)

# Create a BeautifulSoup object with the response from the URL
# Access contents of the web-page using .content
# html_parser is used since our page is in HTML format
soup=BeautifulSoup(page.content,"html.parser")

# Locate elements on page to be scraped
# findAll() locates all occurrences of div tag with the given class name
# stores it in the BeautifulSoup object
weather_forecast = soup.findAll("li", {"class": "forecast-tombstone"})

# Loop through the BeautifulSoup object to extract text text from every class instance using .text
# Store results in a list
for i in weather_forecast:
    i = i.text
    forecast.append(i)

# Print list to remove unicode characters
for day in forecast:
  day=day.replace('This','This ' ) # Introduce space after "This"
  day=day.replace('Showers','Showers ') # Add space after "Showers"
  day=day.replace('Chance','Chance ') # Add space after "Chance"
  day=day.replace('Mostly',' Mostly') # add space before "Mostly"
  day=day.replace('Low',' Low') # add space before "Low"
  day=day.replace('Sunny','Sunny ') # add space after "Sunny"
  day=day.replace('Cloudy','Cloudy ') # add space after "Cloudy"
  day=day.replace('Night',' Night') # add space before "Night"
  print day.upper() # convert all text to capital case and print onscreen
