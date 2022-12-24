# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 06:41:40 2021

@author: M
"""

nation = ['Roman','Egypt','Greek','Chinese','Islamic','Mayan','Persian','Mongol']
golden_age = ['27BC-1453AD','3150BC-30BC','800BC-600AD','221BC-1912AD','750AD-1257AD','2000BC-1540AD','550BC-651AD','1206AD-1368AD']

# Get pairs of elements:
zip_iterator = zip(nation, golden_age)

# Convert to dictionary:
dictionary = dict(zip_iterator)

print("dictionary:", dictionary)


# dictionary[key] = value:
print("Value of 'Roman':", dictionary['Roman'])

# Get key from value in dictionary using dict.item():   
def get_key(dictionary, value):
    for key, val in dictionary.items():
         if val == value:
             return key
 
    return "key doesn't exist"

print("Key of '27BC-1453AD':", get_key(dictionary,'27BC-1453AD'))

# We can also print keys and values using dictionary.keys() and dictionary.values()
