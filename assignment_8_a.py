# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 20:25:25 2021

@author: Aftab Mallick
"""

str1 = input("Enter string: ").split()
ls=[]
for i in str1:

    word_count = str1.count(i)
    ls.append((i,word_count))       


dict1 = dict(ls)

print (dict1)