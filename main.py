import turtle
import random

t = turtle.Turtle()
t.shape('turtle')
t.speed(0)
t.penup()

screen = turtle.Screen()
screen.bgcolor('black')
t.color('white')


def goRandomPlace():
    # Use a breakpoint in the code line below to debug your script.
    i = random.randint(50, 1800)
    j = random.randint(50, 900)
    print("i:", i, "j:", j)


    t.goto(i, j)



while True:
    goRandomPlace()

turtle.mainloop()