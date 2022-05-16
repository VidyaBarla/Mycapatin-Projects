# -*- coding: utf-8 -*-
"""
Created on Mon May 16 21:35:44 2022

@author: Vinnie
"""
X=set(input("Enter a set of Numbers/Letters/Character:"))
Y=set(input("Enter a set of Numbers/Letters/Character:"))
U=X.union(Y)
I=X.intersection(Y)
D=X.difference(Y)
S_D=X.symmetric_difference(Y)
print("Union of set X and Y-",U)
print("Intersection of set X and Y-",I)
print("Difference of set X and Y-",D)
print("Symmetric Difference of set X and Y-",S_D)