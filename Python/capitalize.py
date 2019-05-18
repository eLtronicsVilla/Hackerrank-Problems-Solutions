#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 12:37:30 2019

@author: brgupta
"""

# Problem statement
# https://www.hackerrank.com/challenges/capitalize/problem


import os 

def solve(s):
    new_s = s.split(' ')
    l = []
    for c in new_s:
        l.append(c.capitalize())
    return (' '.join(l))
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
