#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 12:06:00 2019

@author: brgupta
"""

# problem statement:
# https://www.hackerrank.com/challenges/write-a-function/problem

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year %4 == 0 and year %100 !=0 or year % 400 ==0:
        leap = True
    else:
        leap = False
    
    return leap

is_leap(year)