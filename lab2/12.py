#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 16:07:29 2019

@author: student
"""

import turtle
t = turtle
for r in range(7):
    for i in range(50):
        t.forward(1)
        t.right(3.6)
    for i in range(50):
        t.forward(0.3)
        t.right(3.6)
        