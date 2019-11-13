from random import randrange as rnd, choice
import tkinter as tk

# print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class Ball():
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

    def move(self):

        if self.x >= 800 - self.r:
            self.vx = -rnd(1, 5)
        if self.y >= 600 - self.r:
            self.vy = -rnd(1, 5)
        if self.x <= self.r:
            self.vx = rnd(1, 5)
        if self.y <= self.r:
            self.vy = rnd(1, 5)
        self.x += self.vx
        self.y += self.vy
        canv.move(self.id, self.vx, self.vy)


class Ball_2(Ball):

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

    def check_2(self, obj):
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (self.r + obj.r) ** 2:
            return True
        else:
            return False

    def collision_2(self):
        global balls_2
        canv.delete(self.id)
        balls_2.remove(self)
        if len(balls_2) < 15:
            for i in range(2):
                newball = Ball_2()
                balls_2 += [newball]

    def collision_3(self):
        global balls_2
        canv.delete(self.id)
        balls_2.remove(self)


balls_1 = []
balls_2 = []
for i in range(7):
    new_ball = Ball()
    balls_1 += [new_ball]
for i in range(10):
    new_ball = Ball_2()
    balls_2 += [new_ball]


def game():
    global balls_2, balls_1
    for b_1 in balls_1:
        b_1.move()
    for b_2 in balls_2:
        b_2.move()
        for b1 in balls_1:
            if b_2.check_2(b1):
                b_2.collision_3()
        for b in balls_2:
            if b != b_2 and b.check_2(b_2):
                b.collision_2()
    root.after(50, game)


game()
tk.mainloop()
