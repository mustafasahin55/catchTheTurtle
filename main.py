import turtle
import random
import math

# Setup main turtle
t = turtle.Turtle()
t.shape('turtle')
t.speed(0)
t.penup()

# Setup screen
screen = turtle.Screen()
screen.bgcolor('black')
screen.setup(width=500, height=500)
t.color('white')

# Setup score turtle
score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)
score_turtle.penup()
score_turtle.color('white')
score_turtle.goto(0, 220)

# Setup timer turtle
timer_turtle = turtle.Turtle()
timer_turtle.hideturtle()
timer_turtle.speed(0)
timer_turtle.penup()
timer_turtle.color('white')
timer_turtle.goto(0, 200)

# Setup menu turtles
menu_turtle = turtle.Turtle()
menu_turtle.hideturtle()
menu_turtle.speed(0)
menu_turtle.penup()
menu_turtle.color('white')
menu_turtle.goto(0, 100)

timer_menu_turtle = turtle.Turtle()
timer_menu_turtle.hideturtle()
timer_menu_turtle.speed(0)
timer_menu_turtle.penup()
timer_menu_turtle.color('green')
timer_menu_turtle.goto(-100, 0)

target_menu_turtle = turtle.Turtle()
target_menu_turtle.hideturtle()
target_menu_turtle.speed(0)
target_menu_turtle.penup()
target_menu_turtle.color('green')
target_menu_turtle.goto(100, 0)

# Setup buttons for increasing/decreasing timer and target size
timer_increase_turtle = turtle.Turtle()
timer_increase_turtle.hideturtle()
timer_increase_turtle.speed(0)
timer_increase_turtle.penup()
timer_increase_turtle.color('blue')
timer_increase_turtle.goto(-100, 20)
timer_increase_turtle.write("+", align="center", font=("Arial", 16, "normal"))

timer_decrease_turtle = turtle.Turtle()
timer_decrease_turtle.hideturtle()
timer_decrease_turtle.speed(0)
timer_decrease_turtle.penup()
timer_decrease_turtle.color('red')
timer_decrease_turtle.goto(-100, -20)
timer_decrease_turtle.write("-", align="center", font=("Arial", 16, "normal"))

target_increase_turtle = turtle.Turtle()
target_increase_turtle.hideturtle()
target_increase_turtle.speed(0)
target_increase_turtle.penup()
target_increase_turtle.color('blue')
target_increase_turtle.goto(100, 20)
target_increase_turtle.write("+", align="center", font=("Arial", 16, "normal"))

target_decrease_turtle = turtle.Turtle()
target_decrease_turtle.hideturtle()
target_decrease_turtle.speed(0)
target_decrease_turtle.penup()
target_decrease_turtle.color('red')
target_decrease_turtle.goto(100, -20)
target_decrease_turtle.write("-", align="center", font=("Arial", 16, "normal"))

# Setup difficulty buttons
difficulty_menu_turtle = turtle.Turtle()
difficulty_menu_turtle.hideturtle()
difficulty_menu_turtle.speed(0)
difficulty_menu_turtle.penup()
difficulty_menu_turtle.color('white')
difficulty_menu_turtle.goto(0, -40)

easy_turtle = turtle.Turtle()
easy_turtle.hideturtle()
easy_turtle.speed(0)
easy_turtle.penup()
easy_turtle.color('blue')
easy_turtle.goto(-100, -60)
easy_turtle.write("Easy", align="center", font=("Arial", 16, "normal"))

medium_turtle = turtle.Turtle()
medium_turtle.hideturtle()
medium_turtle.speed(0)
medium_turtle.penup()
medium_turtle.color('yellow')
medium_turtle.goto(0, -60)
medium_turtle.write("Medium", align="center", font=("Arial", 16, "normal"))

hard_turtle = turtle.Turtle()
hard_turtle.hideturtle()
hard_turtle.speed(0)
hard_turtle.penup()
hard_turtle.color('red')
hard_turtle.goto(100, -60)
hard_turtle.write("Hard", align="center", font=("Arial", 16, "normal"))

# Setup difficulty indicator line
indicator_line = turtle.Turtle()
indicator_line.hideturtle()
indicator_line.speed(0)
indicator_line.color('white')
indicator_line.penup()
indicator_line.goto(-120, -75)  # Adjust line position
indicator_line.pendown()
indicator_line.goto(120, -75)  # Draw line

# Setup start button turtle
button_turtle = turtle.Turtle()
button_turtle.hideturtle()
button_turtle.speed(0)
button_turtle.penup()
button_turtle.color('green')
button_turtle.goto(0, -120)

cx = 0
cy = 0
tx = 0
ty = 0
score = 0
time_left = 15.0  # Default timer
target_size = 10  # Default target size
difficulty = 1000  # Default difficulty (milliseconds between moves)


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
    if time_left > 0:
        screen.ontimer(goRandomPlace, difficulty)


def clickedPoint(xx, yy):
    global score
    setCursorXY(xx, yy)
    setTurtleXY(t.xcor(), t.ycor())
    distance = math.sqrt((tx - cx) ** 2 + (ty - cy) ** 2)

    if distance < target_size:
        score += 1
        setCursorXY(0, 0)
        updateScore()


def updateScore():
    score_turtle.clear()
    score_turtle.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))


def updateTimer():
    global time_left
    timer_turtle.clear()
    if time_left > 0:
        timer_turtle.write(f"Time left: {round(time_left, 1)}", align="center", font=("Arial", 24, "normal"))
        time_left -= 0.1
        screen.ontimer(updateTimer, 100)  # Update the timer every 100 milliseconds
    else:
        timer_turtle.write("Time's up!", align="center", font=("Arial", 24, "normal"))
        t.hideturtle()  # Hide the turtle when the time is up


def showMenu():
    menu_turtle.write("Game Menu", align="center", font=("Arial", 24, "bold"))
    timer_menu_turtle.write(f"Timer: {int(time_left)}s", align="center", font=("Arial", 16, "normal"))
    target_menu_turtle.write(f"Target Size: {target_size}", align="center", font=("Arial", 16, "normal"))
    button_turtle.write("Start", align="center", font=("Arial", 24, "bold"))
    difficulty_menu_turtle.write("Difficulty:", align="center", font=("Arial", 16, "bold"))


def startGame(x, y):
    if -50 < x < 50 and -130 < y < -110:  # Check if the click is within the button area
        button_turtle.clear()
        screen.onclick(clickedPoint)  # Bind clicks to the game function
        goRandomPlace()
        updateScore()
        updateTimer()


def menuClick(x, y):
    global time_left, target_size, difficulty
    if -120 < x < -80 and 10 < y < 30:  # Increase timer area
        time_left += 5
        timer_menu_turtle.clear()
        timer_menu_turtle.write(f"Timer: {int(time_left)}s", align="center", font=("Arial", 16, "normal"))
    elif -120 < x < -80 and -30 < y < -10:  # Decrease timer area
        if time_left > 5:
            time_left -= 5
        timer_menu_turtle.clear()
        timer_menu_turtle.write(f"Timer: {int(time_left)}s", align="center", font=("Arial", 16, "normal"))
    elif 80 < x < 120 and 10 < y < 30:  # Increase target size area
        target_size += 5
        target_menu_turtle.clear()
        target_menu_turtle.write(f"Target Size: {target_size}", align="center", font=("Arial", 16, "normal"))
    elif 80 < x < 120 and -30 < y < -10:  # Decrease target size area
        if target_size > 5:
            target_size -= 5
        target_menu_turtle.clear()
        target_menu_turtle.write(f"Target Size: {target_size}", align="center", font=("Arial", 16, "normal"))
    elif -120 < x < -80 and -60 < y < -40:  # Easy difficulty area
        indicator_line.clear()
        difficulty = 2000
        indicator_line.penup()
        indicator_line.goto(-118, -60)
        indicator_line.pendown()
        indicator_line.goto(-75, -60)
        indicator_line.penup()
    elif -20 < x < 20 and -60 < y < -40:  # Medium difficulty area
        indicator_line.clear()
        difficulty = 1000
        indicator_line.penup()
        indicator_line.goto(-27, -60)
        indicator_line.pendown()
        indicator_line.goto(20, -60)
        indicator_line.penup()
    elif 80 < x < 120 and -60 < y < -40:  # Hard difficulty area
        indicator_line.clear()
        difficulty = 800
        indicator_line.penup()
        indicator_line.goto(80, -60)
        indicator_line.pendown()
        indicator_line.goto(115, -60)
        indicator_line.penup()
    elif -50 < x < 50 and -130 < y < -110:  # Start button area
        menu_turtle.clear()
        indicator_line.clear()
        timer_menu_turtle.clear()
        target_menu_turtle.clear()
        difficulty_menu_turtle.clear()
        timer_increase_turtle.clear()
        timer_decrease_turtle.clear()
        target_increase_turtle.clear()
        target_decrease_turtle.clear()
        easy_turtle.clear()
        medium_turtle.clear()
        hard_turtle.clear()
        startGame(x, y)


showMenu()
screen.onclick(menuClick)
screen.mainloop()
