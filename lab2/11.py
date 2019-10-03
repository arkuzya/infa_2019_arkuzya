#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 16:03:38 2019

@author: student
"""

import turtle

turtle.speed(10)
for r in range(7):
    for i in range(100):
        turtle.forward(3 + r)
        turtle.right(3.6)
    turtle.left(180)
    for i in range(100):
        turtle.forward(3 + r)
        turtle.right(3.6)