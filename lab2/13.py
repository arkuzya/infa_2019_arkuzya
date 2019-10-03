#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 16:13:12 2019

@author: student
"""

import turtle
t = turtle
t.left(180)
t.color("yellow")
t.begin_fill()
for i in range(100):
    turtle.forward(10)
    turtle.right(3.6)
t.end_fill()
t.penup()
t.right(90)
t.forward(200)
t.left(90)
t.forward(25*4/3)
t.left(90)
t.pendown()
t.color("blue")
t.begin_fill()
for i in range(100):
    turtle.forward(1)
    turtle.right(3.6)
t.end_fill()
t.left(90)
t.penup()
t.forward(50*4/3)
t.pendown()
t.left(90)
t.begin_fill()
for i in range(100):
    turtle.forward(1)
    turtle.right(3.6)
t.end_fill()
t.penup()
t.left(90)
t.forward(25*4/3)
t.left(90)
t.forward(40)
t.pendown()
t.color("black")
t.width(15)
t.forward(40)
t.penup()
t.left(90)
t.forward(60)
t.pendown()
t.color("red")
t.right(90)
for i in range(50):
    turtle.forward(3.9)
    turtle.right(3.6)
