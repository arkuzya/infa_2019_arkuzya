#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 14:48:02 2019

@author: student
"""

import turtle
t=turtle
y=10
for i in range(10):
    for q in range(4):
        t.forward(y)
        t.left(90)
    t.right(90)
    t.penup()
    t.forward(3)
    t.right(90)
    t.forward(3)
    t.left(180)
    t.pendown()
    y=y+6
    