# -*- coding: utf-8 -*-
"""
Created on Mon May 25 18:13:26 2020

@author: Dell
"""


#Assignment 03
#Task 01 - 01 pgm - Write a function to compute 5/0 and use try/except to catch the exceptions.

def divide(x,y):
    try : 
        #Floor Divison : Gives only Fractional Part As Answer 
        result = x//y
        print ("Yeah! Your answer is : ",result)
    except ZeroDivisonError:
        print ("Sorry! You are dividing by zero")
 
divide(5,1)  
    
#Task 01 - 02 Pgm - Implement a Python program to generate all sentences where subject is in ["Americans",
#"Indians"] and verb is in ["Play", "watch"] and the object is in ["Baseball","cricket"].
 
subject = ["Americans","Indians"]
verb = ["Play","watch"]
obj = ["Baseball","cricket"]



#use list comprehension instead of looping over each of the predicates
sentence_list = [(sub+ " " + vb + " "+ ob ) for sub in subject for vb in verb for ob in obj]
for sentence in sentence_list:
    print(sentence)