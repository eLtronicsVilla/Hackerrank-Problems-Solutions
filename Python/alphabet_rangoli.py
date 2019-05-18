#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 12:36:19 2019

@author: brgupta
"""

# problem statement
# https://www.hackerrank.com/challenges/alphabet-rangoli/problem


import string

def print_rangoli(size):
    L = []
    alpha = string.ascii_lowercase
    for i in range(n):
        s = "-".join(alpha[i:n])
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    print('\n'.join(L[:0:-1]+L))
    
