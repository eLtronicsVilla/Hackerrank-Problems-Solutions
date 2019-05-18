#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 12:31:16 2019

@author: brgupta
"""

# Problem statement
# https://www.hackerrank.com/challenges/text-wrap/problem

import textwrap

def wrap(string, max_width):
    txwr = textwrap.TextWrapper(width=max_width)
    txt = txwr.wrap(text =string)
    txt = '\n'.join(txt)
    return txt
