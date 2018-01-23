# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 19:06:20 2018

@author: User
"""
# Problem 1 Handle the exception thrown by the code below by using try and except blocks.
try:
    for i in ['a','b','c']:
        print i**2
except:
    print "There is some Type Error!"
    
# Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'

try:
    x = 5
    y = 0
    z = x/y
except ZeroDivisionError:
    print "There is Zero Division Error"
finally:
    print "All Done"


# Write a function that asks for an integer and prints the square of it. Use a while loop with a try,except, else block to account for incorrect inputs.
    
def ask():
    while True:
        try:
            val= (int(raw_input("Enter the integer Value : ")))
            sqrt=val**2
        except:
            print ("An error occurred! Please try again!")
            continue;
        else:
            print ("The number is an Integer");
            print sqrt
            break;
        finally:
            print ("Finally Block has been excuted")
        

ask()  