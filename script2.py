# Name: Aggeliki Barberopoulou 
# Assignment title: Lab 3 in class exercise
# Time to complete: 15 mins.
# Created: September 9th 2019
# Modified: October 2nd, 2019
# Description: This script calculates rain runoff for a single 
# small area of land and a given rainfall

l=float(input('Enter length of area in feet:'))
w=float(input('Enter width of area in feet:'))

length=l*12 # length of land in inches
print "Area length is:", l # print length in inches
width=w*12 # width of land in inches
print "Area width is:", w # print width in inches
Area = w*l # area of land in square inches
print "Area of land is:", Area ," square feet" # print area

rainwater=input('Enter amount of rain in inches:') #Enter amount of rainfall at prompt
rainfall_inches = Area*rainwater # Rainfall in cubic inches
runoff_gallons=rainfall_inches*0.004329 # Convert rainfall to gallons

# Print results
print "Rainfall_inches is:", rainfall_inches
print "runoff_gallons is:", runoff_gallons
