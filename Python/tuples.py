#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 12:20:44 2019

@author: brgupta
"""

# Problem statement:
# https://www.hackerrank.com/challenges/python-tuples/problem

if __name__ == '__main__':
    l = []
    n = int(input())
    integer_list = l[:n]
    integer_list = map(int, input().split())
    l2 = tuple(integer_list)

    print(hash(l2))
