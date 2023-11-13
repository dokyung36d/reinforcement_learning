import turtle
import math
import numpy as np

ball_turtle = turtle.Turtle()
ball_turtle.shape("circle")

def fastball(speed, ball_turtle):
    ball_turtle.speed(100)
    ball_turtle.penup()
    ball_turtle.goto(0, -200)
    ball_turtle.speed(speed)
    ball_turtle.pendown()
    ball_turtle.setheading(270)
    ball_turtle.goto(0, -350)

def curve(speed, ball_turtle):
    ball_turtle.speed(100)
    ball_turtle.penup()
    ball_turtle.goto(0, -200)
    ball_turtle.speed(speed)
    ball_turtle.pendown()
    ball_turtle.setheading(270)
    ball_turtle.goto(0, -300)
    ball_turtle.circle(50, extent=90)

def fastball_trajectory():
    trajectory = np.zeros((2, 151))
    trajectory[1] = np.arange(-200, -351, -1)

    return trajectory

def curve_trajectory():
    trajectory = np.zeros((2, 151))
    trajectory[1] = np.arange(-200, -351, -1)
    
    for i in range(91):
        trajectory[0][60 + i] = 100 * math.sin(math.radians(i))

    return trajectory