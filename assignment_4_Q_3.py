# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 09:35:36 2021

@author: Aftab Mallick
"""
#Write a python program to reverse a number and check whether it is a palindrome .
n=input("Enter no: ")
reverse_n=n[::-1]
print(f"Reverse ={reverse_n}")
if reverse_n == n :
    print(n,"is a palindrome no.")
else:
    print(n,"is not a palndrome no")