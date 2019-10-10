from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')

canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)

colors = ['red','orange','yellow','green','blue']

OVAL = None
OVAL1 = None
MISHEN = None

#BALL0
def new_ball():
    global x,y,r, OVAL, x1,y1,r1, OVAL1, x2, y2,r2, MISHEN
    canv.delete(ALL)
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    OVAL = canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
    x1 = rnd(100,700)
    y1 = rnd(100,500)
    r1 = rnd(30,50)
    OVAL1 = canv.create_oval(x1-r1,y1-r1,x1+r1,y1+r1,fill = choice(colors), width=0)
    x2 = rnd(100,700)
    y2 = rnd(100,500)
    r2 = rnd(10,80)
    MISHEN = canv.create_rectangle(x2-r2,y2-r2,x2+r2,y2+r2)
    
def update():
	global dx,dy,x,y,r, OVAL
	global dx1,dy1,x1,y1,r1, OVAL1, x2, y2,r2, MISHEN, dx2,dy2
	x += dx
	y += dy
	if x <= r:
		dx = rnd(1,10)
		dy = rnd(-10,10)
	if x >= 800-r:
		dx = -rnd(1,10)
		dy = rnd(-10,10)
	if y >= 600-r:
		dy = -rnd(1,10)
		dx = rnd(-10,10)
	if y <= r:
		dy = rnd(1,10)
		dx = rnd(-10,10)
	canv.move(OVAL,dx,dy)
	x1 += dx1
	y1 += dy1
	if x1 <= r1:
		dx1 = rnd(1,10)
		dy1 = rnd(-10,10)
	if x1 >= 800-r1:
		dx1 = -rnd(1,10)
		dy1 = rnd(-10,10)
	if y1 >= 600-r1:
		dy1 = -rnd(1,10)
		dx1 = rnd(-10,10)
	if y1 <= r1:
		dy1 = rnd(1,10)
		dx1 = rnd(-10,10)
	canv.move(OVAL1,dx1,dy1)
	canv.move(MISHEN,dx2,dy2)
	root.after(50, update)
   
	
#POINTS
def click(event):
	global c
	if (event.x-x)**2+(event.y-y)**2<r**2:
		c = c + 1
		print("Красава1")
		print(c)
	elif (event.x-x1)**2+(event.y-y1)**2<r1**2:
		c = c + 1
		print("Красава2")
		print(c)
	elif event.x-x2 <= r2/2 and event.y-y2 <= r2/2:
		c = c + 1
		print("Вообще затащил")
		print(c)
	elif event.x-x2 <= r2 and event.y-y2 <= r2:
		c = c + 1
		print("Затащил")
		print(c)
	else:
		print ("Лох")
	
		
#CHANGINGBALLS
def fullgame():
	global dy,dx,x,y,r,OVAL,dy1,dx1,x1,y1,r1,OVAL1, x2, y2,r2, MISHEN, dx2,dy2
	dx = rnd(1,5)
	dy = rnd(1,5)
	dx1 = rnd(1,5)
	dy1 = rnd(1,5)
	dx2 = rnd(-8,8)
	dy2 = rnd(-10,10)
	new_ball()
	update()
	root.after(3000,fullgame)

c = 0
fullgame()
canv.bind('<Button-1>', click)
mainloop()



	
