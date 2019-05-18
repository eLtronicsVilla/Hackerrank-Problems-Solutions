#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 12:45:10 2019

@author: brgupta
"""

# Symmetric difference
# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

if __name__ == '__main__':
    n = int(input())
    list1 = []
    list1[:n] = map(int,input().split())

    b = int(input())
    list2 = []
    list2[:b] = map(int,input().split())
    res = ()
    res = set(list1).symmetric_difference(set(list2))
    print(len(res))