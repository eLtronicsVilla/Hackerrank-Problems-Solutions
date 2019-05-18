#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 12:14:07 2019

@author: brgupta
"""

# Problem statement
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    new_arr = list(arr)
    new_arr.sort()
    #print(new_arr)
    count=new_arr.count(new_arr[n-1])
    print(new_arr[n-count-1])
