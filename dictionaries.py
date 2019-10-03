# In class dictionary python example
# Created on October 3d 2019
# by Aggeliki Barberopoulou

#Create this dictionary for a map legend
legend = {0:'no value',1:'deciduous',2:'conifers',3:'industrial',4:'residential',5:'water bodies',6:'agricultural'}

#Write a function that will print all the items using the following structure
def traverse_dict(): # define a function that traverses the dictionary
    for i,k in legend.items(): # for every pair of elements in legend
        print i,k              # print pairs

# call function
traverse_dict()
