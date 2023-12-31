import turtle
import math
import numpy as np

first_turtle = turtle.Turtle()
second_turtle = turtle.Turtle()
ss_turtle = turtle.Turtle()
third_turtle = turtle.Turtle()
left_out_turtle = turtle.Turtle()
center_out_turtle = turtle.Turtle()
right_out_turtle = turtle.Turtle()

turtle_list = [first_turtle, second_turtle, ss_turtle, 
               third_turtle, left_out_turtle, center_out_turtle,
               right_out_turtle]

defender_locations = [[130, -180], [-70, -50], [70, -50],
                      [-130, -180], [-270, 50], [0, 200],
                      [270, 50]]

def set_location_turtle(turtle_list): #순서는 위에 따름
    for i in range(len(turtle_list)):
        turtle_list[i].color("red")
        turtle_list[i].shape("circle")
        turtle_list[i].speed(1000)
        turtle_list[i].penup()
        turtle_list[i].goto(defender_locations[i][0],
                            defender_locations[i][1])
        turtle_list[i].shapesize(stretch_wid=1, stretch_len=1, outline=1)
        
    return turtle_list