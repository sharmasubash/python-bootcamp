# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 17:23:33 2018

@author: User
"""


class Line(object):
    def __init__(self,cord1,cord2):
        self.cord1=cord1;
        self.cord2=cord2;
    def Slope(self): 
        return (float(self.cord2[1])-float(self.cord1[1]))/(self.cord2[0]-self.cord1[0])
    def Distance(self):
        return ((self.cord2[1] - self.cord1[1])**2 + (self.cord2[0]-self.cord1[0])**2)**(0.5)



coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(cord1=coordinate1,cord2=coordinate2)
li.Slope()
li.Distance()

  
class Cylinder(object):
    pi = 3.14;
    def __init__(self,height,radius):
        self.height=height;
        self.radius=radius;
    def surface_area(self):
        return (2 * Cylinder.pi * (self.radius**2)) + (2 * Cylinder.pi * self.radius * self.height)
    def volume(self):
        return (Cylinder.pi*self.height*(self.radius**2))

c = Cylinder(2,3)
print c.volume()
print c.surface_area()       