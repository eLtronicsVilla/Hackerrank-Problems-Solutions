#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 12:34:54 2019

@author: brgupta
"""

# problem statement
# https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formatted(number):
    width = len('{:b}'.format(number))
    for i in range(1,number+1):
        print(str.rjust(str(i),width),str.rjust(str(oct(i)[2:]),width),str.rjust(str(hex(i).upper()[2:]),width),str.rjust(str(bin(i)[2:]),width))
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)