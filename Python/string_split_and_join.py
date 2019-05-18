#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 12:23:21 2019

@author: brgupta
"""

# Problem statement 
# https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def split_and_join(line):
    # write your code here
    line = line.split(" ")
    line = "-".join(line)
    return line 