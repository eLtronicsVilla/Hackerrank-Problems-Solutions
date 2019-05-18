#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 12:40:50 2019

@author: brgupta
"""

# Problem statement
# https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    # this is my code
    for i in range(len(string) // k):
        t = ''
        for c in string[i * k : (i + 1) * k]:
            if c in t:
                continue
            t += c
        print (t)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    