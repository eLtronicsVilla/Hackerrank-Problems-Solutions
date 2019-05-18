#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 12:28:26 2019

@author: brgupta
"""

# problem statement
# https://www.hackerrank.com/challenges/string-validators/problem


def process_string(string):
    check_funs = (str.isalnum,
                  str.isalpha,
                  str.isdigit,
                  str.islower,
                  str.isupper,
                  )
    for fun in check_funs:
        print (any(fun(char) for char in string))

if __name__ == '__main__':
    process_string(input())
        