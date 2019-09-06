# Intro to Python Programming IDCE 302
# Student: Aggeliki Barberopoulou
# This is lab 3 extension to in class exercise
# September 9th 2019

# This script calculates rain runoff of a single 
# small area of land in Kenya with rainfall
# provided by user input

l=50*12 # length of land in inches
w=20*12 # width of land in inches

Area = w*l # area of land in square inches
def runoff_gallons(rainwater):
    rainfall_inches = Area*float(rainwater)
    runoff_gallons = rainfall_inches/231
    print runoff_gallons 
