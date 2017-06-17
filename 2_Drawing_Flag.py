# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 11:18:40 2017

@author: Johnny
"""
import turtle

def draw_one_square(a, b):
    """
    Drawing a square(a,b) with red color.
    """
    turtle.fillcolor('red')
    turtle.pencolor('red')
    turtle.pensize(2)
    turtle.begin_fill()
    for i in [a, b, a, b]:
        turtle.forward(i)
        turtle.left(90)
    turtle.end_fill()

def draw_one_star(length):
    """
    Drawing a star with a parament: base length.
    """
    turtle.fillcolor('yellow')
    turtle.pencolor('yellow')
    turtle.pensize(2)
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(length)
        turtle.left(216)
    turtle.end_fill()

def turtle_move(x, y, d, l):
    """
    Turtle's movement by axis(x, y), direction: d.
    """
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.setheading(d)
    draw_one_star(l)

turtle.reset()
turtle.speed(6)
turtle.hideturtle()   # Hiding turtle(darwing arrow).

turtle.up()
turtle.goto(-300, -150)
turtle.down()
draw_one_square(600, 400)

# Setting the paraments of turtle drawing.
params = [(-260, 160, 0, 110),
          (-125, 180, 120, 35),
          (-90, 140, 90, 35),
          (-95, 90, 75, 35),
          (-130, 50, 60, 35),
         ]
for p in params:
    turtle_move(p[0], p[1], p[2], p[3])

turtle.done()
