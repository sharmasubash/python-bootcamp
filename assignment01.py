# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


# Statments Assignments 


# Use for, split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
x = st.split(' ')
for el in x:
    if el.startswith("s")==True:
        print el
        
#Use range() to print all the even numbers from 0 to 10        
for i in range(0,11):
    if (i %2 == 0):
        print (str(i) + " is an even number")

# Use List comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.       
        
lst = [i for i in range(50) if i % 3 == 0]
print lst

# Go through the string below and if the length of a word is even print "even!"

st = 'Print every word in this sentence that has an even number of letters'
x = st.split(' ')
lst = [z for z in x if len(z)%2==0]
for word in lst:
    print word

'''
 Write a program that prints the integers from 1 to 100. 
 But for multiples of three print "Fizz" instead of the number,
 and for the multiples of five print "Buzz". For numbers
 which are multiples of both three and five print "FizzBuzz".
 '''
 
for i in range(101):
    if i % 3 == 0 and i % 5 != 0:
        print "Fizz"
    elif i % 5 == 0 and i % 3 != 0:
        print "Buzz"
    elif i % 3 == 0 & i % 5 == 0:
        print "FizzBuzz"
    else: 
        print i        

# Use List Comprehension to create a list of the first letters of every word in 
# the string below: 
st = 'Create a list of the first letters of every word in this string'
z = st.split(' ')        
x = [x[0:1] for x in z ]
x

z



    
 