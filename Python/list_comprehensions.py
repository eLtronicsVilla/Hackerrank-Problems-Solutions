#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 12:12:00 2019

@author: brgupta
"""

# problem statement
# https://www.hackerrank.com/challenges/list-comprehensions/problem


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    # ar = []
    # p = 0
    # for i in range (x+1):
    #     for j in range(y+1):
    #         for k in range(z+1):
    #             if i+j+k !=n:
    #                 ar.append([])
    #                  ar[p] = [i,j,k]
    #                 p = p+1
                    
                    
                    
    print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if ((i+j+k)!=n)])

   