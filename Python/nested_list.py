#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 12:16:10 2019

@author: brgupta
"""

# Problem statement
# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    student = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        st = [name,score]
        student.append(st)
        student.sort(key=lambda student : student[1],reverse=False)
    l = len(student)
    c = 0
    new_st = []
    for i in range(l) :
        if student[0][1] == student[i][1]:
            c+=1

    #print(c)
    for i in range(l-c):
        if student[c][1] == student[i+c][1]:
            new_st.append(student[i+c][0])
    
    new_st.sort()
    for i in new_st:
         print(i)
