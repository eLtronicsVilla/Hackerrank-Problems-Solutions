#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 12:25:50 2019

@author: brgupta
"""

# problem statement
# https://www.hackerrank.com/challenges/python-mutations/problem

def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    l = ''.join(l)
    return l

