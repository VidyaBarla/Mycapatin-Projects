# -*- coding: utf-8 -*-
"""
Created on Mon May 16 21:03:41 2022

@author: Vinnie
"""

n=int(input("Enter the number of integers you want in the series:"))
first=0
second=1
print(first,)
print(second,)
for x in range(1,n+1):
    third=first+second
    print(third,)
    first,second=second,third
