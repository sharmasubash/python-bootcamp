# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 12:26:05 2018

@author: User
"""

# Use map to create a function which finds the length of each word in the phrase 
# (broken by spaces) and return the values in a list.
# The function will have an input of a string, and output a list of integers.
def word_lengths(phrase):
    return map(lambda lst : len(lst),phrase.split(' '))


word_lengths('How long are the words in this phrase')


#Use reduce to take a list of digits and return the number that they correspond to. Do not convert the integers to strings!

def digits_to_sum(digits):
    return reduce(lambda x,y: 10*x + y, digits)

digits_to_sum([3,4,3,2,1])

# Use filter to return the words from a list of words which start with a target letter.

def filter_words(word_list, letter):
    return filter( lambda z : z[0]==letter, word_list )

l = ['hello','are','cat','dog','ham','hi','go','to','heart']
filter_words(l,'h')

# Use zip and list comprehension to return a list of the same length where each value is the two strings from L1 and L2 concatenated together with connector between them. Look at the example output below:

def concatenate(L1, L2, connector):
    lst = []
    for lem in zip(L1,L2):
        newstr = lem[0]+connector+lem[1]
        lst.append(newstr)
    return lst

concatenate(['A','B'],['a','b'],'-')

# Use enumerate and other skills to return a dictionary which has the values of the list as keys and the index as the value. You may assume that a value will only appear once in the given list.

def d_list(L):
    dout = {}
    for index, val in enumerate(L):
        dout[val]=index
    return dout
    
d_list(['a','b','c'])

# Use enumerate and other skills from above to return the count of the number of items in the list whose value equals its index.

def count_match_index(L):
    count = 0
    for index , val in enumerate(L):
        if index==val:
            count = count + 1
        else:
            count
    return count

count_match_index([0,2,2,1,5,5,6,10])

