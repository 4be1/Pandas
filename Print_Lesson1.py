#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 16:36:03 2022

@author: word
"""

print('')



print('Hello World')

#Python doesn't care if you use " or '.     Just be consistent 

#escape character to show hello world in quotes

print("\"Hello World \"")


#continue a long sentence/statement for readability (single line)

print('This is a test, please be sure to tip your wait staff \
      on your next trip to disney')
      


# Continuing a statement by using 3 quotations   (seprate lines)   
print("""This is a test, please be sure to tip your wait staff 
            on your next trip to disney""")
            
            
print("We'll first learn how to print.",end="###")
print("Then we'll learn how to comment code")


# Things to comment are process that are being performed in the code.
# e.g. 
# Cleaning Data
# Train model 
# Visualize data


# neat print trick 

print("---------"*15) 


# Concate a string using the + (string only)

print('Can you hear me ' + "now that i make "+"speaking louder")


#Alt way of concat when printing (string or int)
#print('Can you hear me ' , "now that i make ","speaking louder")

print('Can you hear me ',3)


#Below code does not work being python only sees the open and close quotes at the begaining and 
# end and nothing in the middle. Add escapse char if you want to print quotes

#print(""Hi there"")


#SyntaxError: invalid syntax



#print("Hi
#      there")
      
      
#The above code will produce an End of Line SyntaxError becuase you need the newline/escape char  