#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 12:39:25 2019

@author: brgupta
"""

# Problem statement
# https://www.hackerrank.com/challenges/the-minion-game/problem


def minion_game(string):
    # your code goes here
    n = len(string)

    # consonents
    stuart = 0

    # vowels
    kevin = 0
    l = ['A', 'E', 'I', 'O', 'U']
    for i in range(n):
        if string[i] in l:
            kevin += n - i
        else:
            stuart += n - i

    if kevin > stuart:
        print ('Kevin',kevin)
    elif stuart > kevin:
        print ('Stuart', stuart)
    else:
        print ('Draw')
    

if __name__ == '__main__':
    s = input()
    minion_game(s)