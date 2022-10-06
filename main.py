import numpy as np
import pandas as pd
import random 
import os
from list_uktxt import list_convertor 
from lists import *


print("Hello, welcome to the Python random data generator!")
numb_clients = int(input('Generate a number of clients [min 50/max 10.000]: '))    # If the condition doesn't keep the program will shut off
if numb_clients < 50 or numb_clients > 10000:
    exit()
year = str(input('Which year would you like to look up?: '))                      # This will be our spreadsheet name#

#Using the function 'list_convertor()' to convey the txt file into a list#
clients_list = list_convertor("uk.txt")

#This phase is to generate the random data of the company
i = 0
clients = []
brands = []
country = []
while i < numb_clients:
    clients.append(random.choice(clients_list))
    brands.append(random.choice(carbrand))
    country.append(random.choice(location))  # I append random names from the uk_list into my new list which will 
    i += 1                                   #be the amount of clients
        
#Create the DataFrame which we will pass to our Excel Spreadsheet
#First we will pass the lists to a dictionary.
data = {'Client':clients, 'Brand': brands, 'Country': country} 

#Create the DataFrame
data_clients = pd.DataFrame(data)
print(data_clients)

#We create the Excel 

data_clients.to_excel('KaixinSA.xlsx', sheet_name= year)

#Automaticaly you the program execute excel
start_excel = os.startfile('KaixinSA.xlsx')                


