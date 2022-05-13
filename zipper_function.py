# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



def zipper(listA, listB):
    zipped = zip(listA, listB)
    
    return zipped

if __name__ == '_main_':
    
    food = ['pizza', 'sushi', 'jam', 'pho', 'tofu']
    people = ['Bob', 'Kevin', 'Angela', 'Meredith', 'Mena']
    
    result = zipeer(food, people)
    for item in result:
        print(item)
        
        