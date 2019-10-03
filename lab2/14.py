#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 16:43:51 2019

@author: student
"""

import turtle
t = turtle
n = int(input())
for i in range(n):
    t.forward(100)
    t.left(180-180/n)
