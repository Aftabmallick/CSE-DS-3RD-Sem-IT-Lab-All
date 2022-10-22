# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 08:39:24 2022

@author: Aftab Mallick
"""

#Pallindrome or not
n=input("Enter a no: ")
print(f"{n} is a pallindrome.") if n==n[::-1] else print(f"{n} is not a palindrome.")


# find the frequency of a number in an array
a=list(map(int,input("Enter elements in array: ").split()))
n=int(input("Enter no to find frequency: "))
c=0
for i in a:
    if n==i:
        c+=1
print(f"Frequency of {n} is {c}")

#Write a python program to remove duplicate elements from an array
a=list(map(int,input("Enter elements in array: ").split()))
a=set(a)
print(f"Array after removing duplicate element:  {a}")

#sort an array using insertion sort technique
n=int(input("Enter no of Elements: "))
a=list(map(int,input(f"Enter {n} space separated no :  ").split()))
for i in range(1,n):
    key=a[i]
    j=i-1
    while j>=0 and key<a[j]:
        a[j+1]=a[j]
        j-=1
    a[j+1]=key
print(f"Sorted array: {a}")

#display the special numbers lie between 1 to 500
import math as m
print("Special  no are = ")
for i in range(1,500):
    t=i
    sum=0
    while(t>=1):
        rem=t%10
        sum+=m.factorial(rem)
        t=(t//10)
    if sum==i:
        print(i)
#Write a python program to check whether a given matrix is symmetric or not. Use nested 
#list to implement the matrix.
z=0
r =int(input("Enter no of rows : "))
c=int(input("Enter no of rows : "))
parentlist = []
for i in range(0, r):
    str1 =input(f"Enter {c} space separated no: ")
    parentlist.append(str1.split())
for i in range(0, r):
    for j in range(0, c):
        if parentlist[i][j]!=parentlist[j][i]:
            z=10
if z==0:            
    print("Symmetric matrix.")
else:
    print("Not a Symmetric matrix.")
