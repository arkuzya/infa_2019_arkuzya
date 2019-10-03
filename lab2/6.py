#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 15:00:09 2019

@author: student
"""

import turtle
t=turtle
n=int(input())
t.shape("turtle")

for i in range(n):
    t.forward(100)
    t.stamp()
    t.backward(100)
    t.right(360/n)