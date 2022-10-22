# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 08:49:07 2021

@author: Aftab Mallick
"""
""") In general, an equation of the form ax2 + bx + c = 0 is known as quadratic equation.
 Accept the values of a, b, and c from the user and write a python program to calculate the
 roots of the given quadratic equation. You program must be able to handle imaginary roots."""
import cmath

a=int(input("Enter value of a: "))
b=int(input("Enter value of b: "))
c=int(input("Enter value of c: "))

discriminant =(b**2) -(4*a*c)
root1=(-b-cmath.sqrt(discriminant))/(2*a)
root2=(-b+cmath.sqrt(discriminant))/(2*a)
print('roots are{0} and {1}'.format(root1,root2))