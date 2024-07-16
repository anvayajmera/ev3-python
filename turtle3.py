import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Turtle Art 3")

colors = ["red", "green", "blue", "yellow", "purple", "orange", "pink", "white", "cyan"]

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

def draw_hexagon(size, color):
    hexagon = turtle.Turtle()
    hexagon.speed(0)
    hexagon.color(color)
    for _ in range(6):
        hexagon.forward(size)
        hexagon.right(60)
    hexagon.hideturtle()

for _ in range(5):
    draw_hexagon(random.randint(50, 150), random.choice(colors))

def draw_fractal_tree(t, length, level):
    if level == 0:
        return
    t.forward(length)
    t.left(30)
    draw_fractal_tree(t, length * 0.7, level - 1)
    t.right(60)
    draw_fractal_tree(t, length * 0.7, level - 1)
    t.left(30)
    t.backward(length)

tree = turtle.Turtle()
tree.speed(0)
tree.color("white")
tree.left(90)
tree.up()
tree.backward(100)
tree.down()
draw_fractal_tree(tree, 100, 5)
tree.hideturtle()

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

def random_walk(turtle, steps):
    directions = [0, 90, 180, 270]
    for _ in range(steps):
        turtle.color(random.choice(colors))
        turtle.forward(20)
        turtle.setheading(random.choice(directions))

walker = turtle.Turtle()
walker.speed(0)
walker.width(2)
random_walk(walker, 200)
walker.hideturtle()

def draw_spiral():
    spiral = turtle.Turtle()
    spiral.speed(0)
    for i in range(100):
        spiral.color(random.choice(colors))
        spiral.forward(i * 2)
        spiral.right(45)
    spiral.hideturtle()

draw_spiral()

def draw_triangle(size, color):
    triangle = turtle.Turtle()
    triangle.speed(0)
    triangle.color(color)
    for _ in range(3):
        triangle.forward(size)
        triangle.right(120)
    triangle.hideturtle()

for _ in range(5):
    draw_triangle(random.randint(50, 150), random.choice(colors))

def draw_square(size, color):
    square = turtle.Turtle()
    square.speed(0)
    square.color(color)
    for _ in range(4):
        square.forward(size)
        square.right(90)
    square.hideturtle()

for _ in range(5):
    draw_square(random.randint(50, 150), random.choice(colors))

def draw_random_lines():
    lines = turtle.Turtle()
    lines.speed(0)
    lines.width(2)
    for _ in range(100):
        lines.color(random.choice(colors))
        lines.forward(random.randint(50, 150))
        lines.right(random.randint(0, 360))
    lines.hideturtle()

draw_random_lines()

screen.mainloop()
