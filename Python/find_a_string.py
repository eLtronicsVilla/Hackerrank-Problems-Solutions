#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 12:26:59 2019

@author: brgupta
"""

# Problem statement:
# https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    cnt = 0
    len_ss = len(sub_string)
    for i in range(len(string) - len_ss + 1):
        if string[i:i+len_ss] == sub_string:
            cnt += 1
    return cnt