# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 16:06:39 2018

@author: User
"""

# Write a function that computes the volume of a sphere given its radius.

def vol(rad):
    volume = ((4/3)*3.14)*(rad**3)
    return volume

print vol(45)

# Write a function that checks whether a number is in a given range (Inclusive of high and low)

def ran_check(num,low,high):
    if low<=num<=high:
        print "Yes"
    else:
        print "No"
        
'''
Write a Python function that accepts a string and calculate the number of 
upper case letters and lower case letters.     
'''

def find_upper_and_lower_char(st):
    words = st.split(' ')
    lst_of_list = [y for z in words for y in z]
    all_upper_letters = len([z for z in lst_of_list if z.isupper()==True])
    all_lower_letters = len([z for z in lst_of_list if z.islower()==True])
    print "No. of Upper case characters : " + str(all_upper_letters);
    print "No. of Lower case Characters : " + str(all_lower_letters);

find_upper_and_lower_char("Hello Mr. Rogers, how are you this fine Tuesday?")

'''
Write a Python function that takes a list and returns a new list with unique elements of the first list.
'''

def rem_dup_elements(lst):
    lst = set(lst);
    lst = list(lst);
    return lst
  
print rem_dup_elements([1,2,3,4,5,6,7,8,9,1,1,1,1,1,1,1,1,1,1])  

# Write a Python function that checks whether a passed string is palindrome or not.

def palin(st):
    lst  = [z for z in st]  
    lst.reverse()
    if st == "".join(lst):
        return st + " is a palindrone"
    else:
        return st + " is not palindrone"
    
print (palin('maan')) 

# Write a Python function to check whether a string is pangram or not.

import string;

def isPangram(st, alphabet = string.ascii_lowercase):
    st = st.lower()
    lst = [s for s in st]
    lst = set(lst)
    lst=list(lst)
    lst.remove(' ')
    lst.sort()
    if "".join(lst) == alphabet:
        return "the string is pangram"
    else:
        return "the string not a pangram"
    
