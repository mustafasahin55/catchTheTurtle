import turtle
import random
import time
import math

t = turtle.Turtle()
t.shape('turtle')
t.speed(0)
t.penup()

screen = turtle.Screen()
screen.bgcolor('black')
screen.setup(width=500, height=500)
t.color('white')

global cx
global cy
cx = 0
cy = 0
global tx, ty
tx = 0
ty = 0

score = 0


def setCursorXY(x_n, y_n):
    global cx, cy
    cx = x_n
    cy = y_n


def setTurtleXY(x_n, y_n):
    global tx, ty
    tx = x_n
    ty = y_n


def goRandomPlace():
    i = random.randint(-225, 225)
    j = random.randint(-225, 225)
    t.goto(i, j)


def clickedPoint(xx, yy):
    setCursorXY(xx, yy)


while True:
    goRandomPlace()
    screen.onclick(clickedPoint)
    setTurtleXY(t.xcor(), t.ycor())
    distance = math.sqrt((tx - cx) ** 2 + (ty - cy) ** 2)
    print("distance:", distance)

    if distance < 20:
        print("if")
        score += 1  # score'u 1 artır
        setCursorXY(0, 0)

    print('x:', cx, 'y:', cy, "tx:", tx, "ty:", ty, 'score:', score)
    time.sleep(2)
turtle.mainloop()
