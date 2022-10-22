# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 19:48:34 2021

@author: Aftab Mallick
"""

def wellbrackted(exp):
    stck=[]
    for i in exp:
        if i=='(':
            stck.append('(')
        if i==')':
            try:
                stck.pop()
            except IndexError:
                return False
    if len(stck)==0:
        return True
    else:
        return False
exp=input('Enter an expression: ')
if wellbrackted(exp):
    print(exp,"is well brackted")
else:
    print(exp,"isn't well brackted")