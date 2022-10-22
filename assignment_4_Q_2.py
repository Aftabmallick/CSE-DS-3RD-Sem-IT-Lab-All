# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 09:27:28 2021

@author: Aftab Mallick
"""
#Write a python program to generate all prime numbers within a range ,where range is user input .
lr=int(input("Enter lower range: "))
ur=int(input("Enter upper range: "))

for no in range(lr,ur+1):
    if no > 1:
        for i in range(2,no):
            if(no%i)==0:
                break
        else:
            print(no)