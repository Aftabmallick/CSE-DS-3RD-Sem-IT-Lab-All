# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 10:03:14 2021

@author: Aftab Mallick
"""

class StLine:
    def __init__(self,L=0):
        print("Object created")
        self.length=L
    def display(self):
          print("lenth of the square",self.length)
        
        
class Square(StLine):
    def __init__(self,L):
    
       super().__init__(L)
      #self.length=L
    #def display(self):
     #     print("lenth of the square",self.length)
        
    def calc_area(self):
        return self.length*self.length


class Cube(Square):
    def __init__(self,length=0):
        super().__init__(length)
        
    def s_area(self):
        self.area=super().calc_area()
        return 6*self.area
        
    
    
stl=StLine(20)
sq=Square(25)

cube1=Cube(10)
print(cube1.s_area())
class triangel():
    def __init__(self,Base=0,Height=0):
        self.Base=Base
        self.Height=Height
    def area(self):
        return .5*self.Base*self.Height
class rectangle():
    def __init__(self,Base=0,Height=0):
        self.Base=Base
        self.Height=Height
    def area(self):
        return self.Base*self.Height

    
