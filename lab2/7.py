#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 15:08:08 2019

@author: student
"""

import turtle
t = turtle
t.speed(0)
g=0
for i in range(500):
    t.forward(0.03*g)
    t.left(3)
    g=g+1

