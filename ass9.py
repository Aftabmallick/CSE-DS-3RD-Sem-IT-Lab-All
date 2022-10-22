# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 10:08:25 2021

@author: Aftab Mallick
"""

class circle:
    def __init__(self,radius=0):
        self.r=radius
    def get_radius(self):
        self.r=int(input("Enter Radius of the circle: "))
    def calc_area(self,r):
        return 3.14*self.r**2

circle1=circle()
circle1.get_radius()
area=circle1.calc_area(circle1.r)
print(f"Area of circle is {area}")