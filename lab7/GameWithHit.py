from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH,expand=1)

colors = ['red','orange','yellow','green','blue']
	
class Sharik:
		def __init__(self,x,y,Vx,Vy,Ax,Ay,r):
				self.x = x
				self.y = y
				self.Vx = Vx
				self.Vy = Vy
				self.Ax = Ax
				self.Ay = Ay
				self.r = r
				self.ball = canv.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, fill=choice(colors), width=0)

								
		def hit(self, ball_2):
				if (ball_2.x != self.x) and ( (ball_2.x-self.x) ** 2 + (ball_2.y - self.y) ** 2 <= ( (self.r + ball_2.r)  ** 2)):
						self.Vx, ball_2.Vx = ball_2.Vx, self.Vx
						self.Vy, ball_2.Vy = ball_2.Vy, self.Vy
						while  (ball_2.x-self.x) ** 2 + (ball_2.y - self.y) ** 2 <= ( (self.r + ball_2.r)  ** 2):
								canv.move(self.ball, self.Vx, self.Vy)
								self.x += self.Vx
								self.y += self.Vy
								canv.move(ball_2.ball, ball_2.Vx, ball_2.Vy)
								ball_2.x += ball_2.Vx
								ball_2.y += ball_2.Vy

		def update(self):
				global balls
				self.x += self.Vx
				self.y += self.Vy
				if self.x <= self.r:
						self.Vx = rnd(1,5)
						self.Vy = rnd(-5,5)
				if self.x >= 800-self.r:
						self.Vx = -rnd(1,5)
						self.Vy = rnd(-5,5)
				if self.y >= 600-self.r:
						self.Vy = -rnd(1,5)
						self.Vx = rnd(-5,5)
				if self.y <= self.r:
						self.Vy = rnd(1,5)
						self.Vx = rnd(-5,5)
				canv.move(self.ball,self.Vx,self.Vy)
				for i in balls:
						self.hit(i)
				root.after(20, self.update)

balls = []
def fullgame():
		global balls
		canv.delete(ALL)
		ball1 = Sharik(rnd(50, 750), rnd(50, 550), rnd(-5, 5), rnd(-5, 5), 0, 0, rnd(20, 40))
		balls.append(ball1)
		ball2 = Sharik(rnd(50, 750), rnd(50, 550), rnd(-5, 5), rnd(-5, 5), 0, 0, rnd(20, 40))
		balls.append(ball2)
		ball3 = Sharik(rnd(50, 750), rnd(50, 550), rnd(-5, 5), rnd(-5, 5), 0, 0, rnd(20, 40))
		balls.append(ball3)
		ball4 = Sharik(rnd(50, 750), rnd(50, 550), rnd(-5, 5), rnd(-5, 5), 0, 0, rnd(20, 40))
		balls.append(ball4)
		ball5 = Sharik(rnd(50, 750), rnd(50, 550), rnd(-5, 5), rnd(-5, 5), 0, 0, rnd(20, 40))
		balls.append(ball5)
		ball1.update()
		ball2.update()
		ball3.update()
		ball4.update()
		ball5.update()



fullgame()
mainloop()
