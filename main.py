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

global x
global y
x = 0
y = 0
score = 0
def setX(x_n):
    global x
    x = x_n
def setY(y_n):
    global y
    y = y_n

def goRandomPlace():
    i = random.randint(-225, 225)
    j = random.randint(-225, 225)
    t.goto(i, j)


def clickedPoint(xx,yy):
    setX(xx)
    setY(yy)

while True:
    goRandomPlace()
    screen.onclick(clickedPoint)
    t_x, t_y = t.pos()
    distance = math.sqrt((t_x - x)**2 + (t_y - y)**2)
    if distance < 20:
        print("if")
        score += 1  # score'u 1 artır
        setX(0)
        setY(0)

    print('x:',x,'y:',y,"tx:",t_x,"ty:",t_y,'score:',score)
    time.sleep(2)
turtle.mainloop()
