#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 08:56:08 2019

@author: brgupta
"""

# problem statement:
# https://www.hackerrank.com/challenges/py-if-else/problem

if __name__ == '__main__':
    n = int(input())
    if n%2 != 0:
        print("Weird")
    elif(n >= 2 and n<=5):
        print("Not Weird")
    elif(n >=6 and n<=20):
        print("Weird")
    elif(n > 20):
        print("Not Weird")