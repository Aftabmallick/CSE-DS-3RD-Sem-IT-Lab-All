# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 08:59:23 2022

@author: Aftab Mallick
"""

class SqrArea():
    def calc_area(self):
        return self.length*self.length
class SqrPeri():
    def calc_peri(self):
        return 4*self.length
class Square(SqrArea,SqrPeri):
    def __init__(self,length):
        self.length=length
        print("object created of class Square")
    def show(self):
        print("Area :",self.calc_area())
        print("Peri :",self.calc_peri())
        
sq1=Square(int(input("Enter length: ")))
print(sq1.show())