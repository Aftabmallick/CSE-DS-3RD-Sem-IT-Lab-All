# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 10:59:04 2022

@author: Aftab Mallick
"""

f2=open("test321.txt",'w')
for i in range(1,11):
    f2.write(str(i)+" ")
f2.close()
f2=open("test321.txt",'r')
print(f2.tell())


f2.seek(0,2)
print(f2.tell())


