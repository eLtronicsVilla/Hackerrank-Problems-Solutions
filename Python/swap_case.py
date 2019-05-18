#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 12:21:49 2019

@author: brgupta
"""

#Problem statement:
# https://www.hackerrank.com/challenges/swap-case/problem


def swap_case(s):
    new_s = []
    for ch in s:
        if ch.islower():
            new_s.append(ch.upper())
        elif ch.isupper():
            new_s.append(ch.lower())
        else:
            new_s.append(ch)

    new_s = ''.join(new_s)
    return (new_s)