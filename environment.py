import turtle

# Set up the turtle screen
# screen = turtle.Screen()
# screen.setup(width=1000, height=750)

# Create the turtle

# Function to draw a baseball diamond
def draw_baseball_diamond():
    my_turtle = turtle.Turtle()
    my_turtle.shape("turtle")
    my_turtle.speed(100)
    my_turtle.penup()
    my_turtle.goto(0, -350)
    my_turtle.pendown()
    my_turtle.goto(150, -200)
    my_turtle.goto(0, -50)
    my_turtle.goto(-150, -200)
    my_turtle.goto(0, -350)
    my_turtle.goto(500, 150)
    my_turtle.goto(0, -350)
    my_turtle.goto(-500, 150)
    my_turtle.penup()
    my_turtle.goto(0, -450)
    my_turtle.pendown()
    my_turtle.circle(400)
    my_turtle.pendown()


bat_x = 0
global_angle = 0


#bat를 돌리는 것을 실제 화면으로 보여주는 무리인 듯..
def bat(start_time): # - < angle < 

    bat_turtle = turtle.Turtle()
    bat_turtle.shape("square")
    bat_turtle.shapesize(stretch_wid=0.5, stretch_len=6, outline=1)
    bat_turtle.penup()
    bat_turtle.goto(bat_x, -350)
    for i in range(270, 450, 3):
        bat_turtle.setheading(i % 360)
        global_angle = i % 360 



# draw_baseball_diamond()
# bat(1)
# screen.exitonclick()