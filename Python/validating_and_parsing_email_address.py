#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 12:46:20 2019

@author: brgupta
"""

# Problem statement
# https://www.hackerrank.com/challenges/validating-named-email-addresses/problem

import re

for i in range(int(input())):
    x, y = input().split(' ')
    m = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', y)
    if m:
        print(x,y)