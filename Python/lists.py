#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 12:19:22 2019

@author: brgupta
"""

# problem statement
# https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    l = []
    N = int(input())
    for i in range(N):
        c = input().split()
        if len(c) == 3:
            eval("l." + c[0] + "(" + c[1] + "," + c[2] + ")")
        elif len(c) == 2:
            eval("l." + c[0] + "(" + c[1] + ")" )
        elif c[0] == 'print':
            print(l) 
        else:
             eval("l." + c[0] + "()")

