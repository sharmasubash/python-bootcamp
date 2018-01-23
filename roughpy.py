# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 15:22:05 2018

@author: User
"""

z = [1,2,3,4,5,6]
z.append(9)
z

square = lambda num:num**2;
square(3)

add_num = lambda num1,num2: num1 + num2;
add_num(1,2)
reduce()

name = "subash"

def greet():
    name = "sharma"
    def hello():
        print name + " subash"
    return hello()
    
greet()
name    

x = 30;
def func():
    global x ;
    x = 2;
    return  x
print func()
x

class Sample(object):
    pass

x = Sample()
type(x)

class Dog(object):
    species = 'mammal';
    def __init__(self,breed):
        self.breed=breed
        
x = Dog(breed='chua')
print x.breed
print x.species  


class Circle(object):
    pi = 3.14
    def __init__(self,radius=1):
        self.radius=radius
    def area(self):
        return ((self.radius**2)*Circle.pi)
    def set_radius(self,new_radius):
        self.radius=new_radius
        
z = Circle(radius=100)        

z.area()
z.set_radius(new_radius=10)
z.radius
        
class Animal(object):
    def __init__(self):
        print "Animal Created"
    def whoAmI(self):
        print "Animal"
    def eat(self):
        print "eating"
        
x = Animal()
x.whoAmI() 

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print "Dog Created"
    def whoAmI(self):
        print ("Dog")       
    def bark(self):
        print ("Woof")
        
y = Dog()  
y.bark()
y.whoAmI()
  
class Book(object):
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    def __str__(self):
        return "Title %s, Author %s, Pages %s" %(self.title,self.author,self.pages) 
    
b = Book('python','subash',200)  
print b  


try:
    2 + 's';
except TypeError:
    print ("There was a type error")
finally:
    print ("this is the final message")
import os
os.getcwd()


try:
    f = open('testfile','w')
    f.write("i am awesome")
except:
    print ("error in writing file")
else:
    print ("Code executed!")
    
def check_amigo():
    while True:
        try:
            val = int(raw_input("please enter an integer: "))
        except:
            print ("Not an Integer")
            continue
        else:
            print ("Integer has been found")
            break
        finally:
            print ("Finally Block has been executed")
        print val
       
check_amigo()    


def make_sum(a,b):
    return a + b

map(lambda a: (a*(-1)),[10])

lst = [12,23,845,56]
reduce(lambda a,b : a if a > b else b , lst)

def check_even(num):
    if num%2 == 0:
        return True
    else:
        return False

lst = range(11)
filter(check_even,lst)

filter(lambda num: num%2==0 ,lst)


lst1 = [1,2,3]
lst2 = [4,1,6]
zip(lst1,lst2)

map(lambda pair:max(pair),zip(lst1,lst2))

dict1 = {'a':1,'b':2}
dict2 = {'c':3,'d':4}

def switchval(dict1,dict2):
    dout={}
    for dict1key, dict2val in zip(dict1,dict2.itervalues()):
        dout[dict1key]=dict2val
    return dout

switchval(dict1,dict2)


for index,elem in enumerate(lst):
    if index >= 2:
        break
    print index,elem
        
lst = [True,True,False,False]
print all(lst)
print any(lst)

def hello(name ='Jose'):
    return "Hello " + name
print hello()
greet = hello
print greet()

def hello(name = 'Jose'):
    def greet():
        return ('\t i am inside greet() function')
    def welcome():
        return ("\n \t \t i am inside welcome() function")
    if name=='Jose':
        return greet
    else:
        return welcome
    

x=hello()   
print x()

def hello():
    return "hello"
def other(func):
    print "other code goes in here!"
    print func()

other(hello)


def new_decorator(func):
    def wrap_func():
        print "this statement executes before func"
        func()
        print "code here will get executed after func"      
    return wrap_func
@new_decorator
def func_needs_decorator():
    print "This function needs a decorator"


func_needs_decorator()

def gencubes(n):
    lst = []
    for num in range(n):
        lst.append(num**3)
    yield lst
        
for x in gencubes(10):
    print x
        
    
    
        
        