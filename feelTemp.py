# Intro to Python Programming
# IDCE 319 Lab 3
# Created by Aggeliki Barberopoulou
# on September 13th 2019 (this is a Friday and 13th lab!!!!)
# Time spent ~15 mins


# Function converts a given temperature into four categories
# hot, warm, cool and cold using four criteria (range of temperature)
# and prints a statement based on user input

x=int(input("Enter temperature in Fahrenheit: ")) # requires user input



def feelTemp(x):
        
    if x>=100:
     print("It is hot.")  # Temperature over 100 are hot
    elif x>=70 and x<100: # Temperatures between 70 and 100 are warm 
     print("It is warm.") # Temperatures between 32 and 70 are cool
    elif x>=32 and x<70:  # All remaining temperatures are cold
     print("it is cool.")
    else:
         print("It is cold!")

         

feelTemp(x)         
