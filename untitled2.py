# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 10:03:38 2021

@author: Aftab Mallick
"""

class Circle():
    def _init_(self,r=None):
        if r is None:
            self.radius = eval(input('enter the radius: '))
        else:
            self.radius = r
            print("a circle has been created")
        
    def get_radius(self):
        return self.radius
    
    def calc_area(self):
        return 3.14*self.radius**2
    
    def _del_(self):
        print("object destroyed")

        
  
class Cylinder(Circle):
    def _init_(self,h = None,r = None):
        if h is None:
            self.height = eval(input('input the height'))
        else:
            self.height = h
        if r is None:
            super()._init_()
        else:
            super()._init_(r)
        print("a cylinder has been created")
    def calc_area(self):
        return 2*3.14*self.radius*(self.radius+self.height)
cylinder1=Circle().Cylinder()
cylinder1.get_radius()
