import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Epic Turtle Art")

colors = ["red", "green", "blue", "yellow", "purple", "orange", "pink", "white", "cyan"]

def draw_sunset():
    sunset = turtle.Turtle()
    sunset.speed(0)
    sunset.hideturtle()
    screen.bgcolor("midnightblue")
    sunset.color("orange")
    sunset.begin_fill()
    sunset.circle(150)
    sunset.end_fill()
    sunset.color("red")
    sunset.begin_fill()
    sunset.circle(100)
    sunset.end_fill()
    sunset.color("yellow")
    sunset.begin_fill()
    sunset.circle(50)
    sunset.end_fill()

draw_sunset()

def draw_fractal_square(t, size, level):
    if level == 0:
        for _ in range(4):
            t.forward(size)
            t.right(90)
    else:
        for _ in range(4):
            draw_fractal_square(t, size / 3, level - 1)
            t.forward(size)
            t.right(90)

fractal_square = turtle.Turtle()
fractal_square.speed(0)
fractal_square.color(random.choice(colors))
draw_fractal_square(fractal_square, 200, 4)
fractal_square.hideturtle()

def draw_koch_snowflake(t, size, level):
    if level == 0:
        t.forward(size)
        return
    size /= 3.0
    draw_koch_snowflake(t, size, level-1)
    t.left(60)
    draw_koch_snowflake(t, size, level-1)
    t.right(120)
    draw_koch_snowflake(t, size, level-1)
    t.left(60)
    draw_koch_snowflake(t, size, level-1)

snowflake = turtle.Turtle()
snowflake.speed(0)
snowflake.color(random.choice(colors))
for _ in range(3):
    draw_koch_snowflake(snowflake, 300, 4)
    snowflake.right(120)
snowflake.hideturtle()

def draw_pattern():
    pattern = turtle.Turtle()
    pattern.speed(0)
    for _ in range(36):
        pattern.color(random.choice(colors))
        for _ in range(4):
            pattern.forward(100)
            pattern.right(90)
        pattern.right(10)
    pattern.hideturtle()

draw_pattern()

def draw_flower():
    flower = turtle.Turtle()
    flower.speed(0)
    flower.color(random.choice(colors))
    for _ in range(36):
        for _ in range(2):
            flower.circle(50, 60)
            flower.left(120)
        flower.left(10)
    flower.hideturtle()

draw_flower()

def draw_star(size, color):
    star = turtle.Turtle()
    star.speed(0)
    star.color(color)
    star.begin_fill()
    for _ in range(5):
        star.forward(size)
        star.right(144)
    star.end_fill()
    star.hideturtle()

for _ in range(5):
    draw_star(random.randint(20, 100), random.choice(colors))

def draw_spiral():
    spiral = turtle.Turtle()
    spiral.speed(0)
    for i in range(100):
        spiral.color(random.choice(colors))
        spiral.forward(i * 2)
        spiral.right(45)
    spiral.hideturtle()

draw_spiral()

def draw_random_walk(turtle, steps):
    directions = [0, 90, 180, 270]
    for _ in range(steps):
        turtle.color(random.choice(colors))
        turtle.forward(20)
        turtle.setheading(random.choice(directions))

walker = turtle.Turtle()
walker.speed(0)
walker.width(2)
draw_random_walk(walker, 200)
walker.hideturtle()

def draw_mandala(size):
    mandala = turtle.Turtle()
    mandala.speed(0)
    mandala.color(random.choice(colors))
    for _ in range(6):
        mandala.circle(size)
        mandala.right(60)
    mandala.hideturtle()

for _ in range(3):
    draw_mandala(random.randint(50, 150))

screen.mainloop()
