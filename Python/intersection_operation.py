#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 12:41:46 2019

@author: brgupta
"""

# Problem statement
# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem



if __name__ == '__main__':
    n = int(input())
    list1 = []
    list1[:n] = input().split()
    
    
    b = int(input())
    list2 = []
    list2[:b] = input().split()
    res = ()
    res = (set(list1).intersection(set(list2)))
    print(len(res))
