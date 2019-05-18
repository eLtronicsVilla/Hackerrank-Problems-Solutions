#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 12:33:31 2019

@author: brgupta
"""

# problem statement
# https://www.hackerrank.com/challenges/designer-door-mat/problem


if __name__ == '__main__':
    M,N = map(int,input().split())
    # print(M)
    # print(N)
    pattern = [('.|.'*(2*i+1)).center(N,'-') for i in range(M//2)]
    print('\n'.join(pattern + ['WELCOME'.center(N,'-')] + pattern[::-1]))
