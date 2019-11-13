from random import randrange as rnd, choice
import tkinter as tk

# constants
LENGTH = 800
WIDTH = 600
root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class Ball:

    def __init__(self):
        self.x = rnd(50, 750)
        self.y = rnd(50, 550)
        self.r = rnd(5, 45)
        self.vx = rnd(-5, 5)
        self.vy = rnd(-5, 5)
        self.ay = 0
        self.ax = 0

    def move(self):
        if self.x >= LENGTH - self.r:
            self.vx = -rnd(1, 5)
        if self.y >= WIDTH - self.r:
            self.vy = -rnd(1, 5)
        if self.x <= self.r:
            self.vx = rnd(1, 5)
        if self.y <= self.r:
            self.vy = rnd(1, 5)
        self.x += self.vx
        self.y += self.vy
        canv.move(self.id, self.vx, self.vy)

    def check(self, obj):
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (self.r + obj.r) ** 2:
            return True
        else:
            return False


class Ball2(Ball):

    def __init__(self):

        self.x = rnd(50, 750)
        self.y = rnd(50, 550)
        self.r = rnd(5, 45)
        self.vx = rnd(-5, 5)
        self.vy = rnd(-5, 5)
        self.ay = 0
        self.ax = 0
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill='red'
        )

    def collision_2(self):
        global balls_1, balls_2
        canv.delete(self.id)
        balls_2.remove(self)
        new_one_ball = Ball1()
        balls_1 += [new_one_ball]
        new_one_ball = Ball2()
        balls_2 += [new_one_ball]


class Ball1(Ball):

    def __init__(self):
        self.x = rnd(50, 750)
        self.y = rnd(50, 550)
        self.r = rnd(5, 45)
        self.vx = rnd(-5, 5)
        self.vy = rnd(-5, 5)
        self.ay = 0
        self.ax = 0
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill='purple'
        )

    def collision_1(self):
        global balls_1
        canv.delete(self.id)
        balls_1.remove(self)


def set_balls():
    global balls_1, balls_2
    balls_1 = []
    balls_2 = []
    for i in range(10):
        new_ball = Ball1()
        balls_1 += [new_ball]
    for i in range(10):
        new_ball = Ball2()
        balls_2 += [new_ball]


def game():
    global balls_2, balls_1
    for b_1 in balls_1:
        b_1.move()
        for b in balls_1:
            if b != b_1 and b_1.check(b):
                b.collision_1()
    for b_2 in balls_2:
        b_2.move()
        for b in balls_2:
            if b != b_2 and b.check(b_2):
                b.collision_2()
    root.after(50, game)


set_balls()
game()
tk.mainloop()
