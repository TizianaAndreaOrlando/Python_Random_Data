import pandas as pd
import numpy as np
import random
from lists import *

clients = int(input('Input the number of clients of the month: '))
year = int(input('Input the year please '))

namegenerator = str(input('Would you like to get a list of users? yes / no ')).lower()
"""Random User generator"""

if namegenerator == 'yes':

    df = pd.read_csv('uk.txt', header=None)

    names = df[0].astype(str).tolist()

    i = 0
    for x in names:
        while i < clients:
            print(random.choice(names))
            i = i + 1
"""Random brand generator"""
brandgenerator = input(str('would you like to get a list of brands? yes / no ')).lower()

if brandgenerator == 'yes':

    l = 0
    for z in carbrand:
        while l < clients:
            print(random.choice(carbrand))
            l = l + 1

logenerator = str(input('would you like to get a list of locations? yes / no ')).lower()
"""Random Location generator"""

if logenerator == 'yes':
    k = 0
    for y in location:
        while k < clients:
            print(random.choice(location))
            k = k + 1

"""days generator"""
daysgenerator = input(str('would you like to get a list of the number of rent days per user? yes / no ')).lower
if daysgenerator == 'yes':

    m = 0
    while m <clients:
        x = random.randint(1, 15)
        print(x)
        m = m + 1

"""Date generator"""
"""Note: It's limited to the 30 days skipping the 31 day for the simplicity of the function"""
dategenerator = input(str('Would you like to get a date? yes / no ')).lower()
if dategenerator == 'yes':

    n = 0
    while n <clients:
        day = random.randrange(1, 30)
        month = random.randrange(1, 12)
        if month == 2 and day >29:
            day = day - 1
        print(day, '/', month, '/', year)
        n = n + 1

print('Thank you so much for using this program, have a nice day! \n-- Orlando tiziana--')


