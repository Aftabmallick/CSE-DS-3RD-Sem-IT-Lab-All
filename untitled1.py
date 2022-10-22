# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 14:00:37 2022

@author: Aftab Mallick
"""

class PowerSet():
    def __init__(self,x):
        if type(x)==set:
            self.x=x
        else:
            print("not a set")