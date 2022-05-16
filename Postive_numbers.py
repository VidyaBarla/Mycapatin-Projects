# -*- coding: utf-8 -*-
"""
Created on Tue May 10 00:22:03 2022

@author: Vinnie
"""
List1=eval(input("Enter a list of numbers:"))
List2=[]
for i in range(0,len(List1)):
    x=List1[i]
    if x%2==0:
        List2.append(x)
print("The given List:",List1)
print("The list of even numbers:",List2)
        
        