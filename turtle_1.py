import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.setup(width=1000, height=750)

# Create the turtle
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.speed(100)
# Function to draw a baseball diamond
def draw_baseball_diamond():
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


ball_turtle = turtle.Turtle()
ball_turtle.shape("circle")

def fastball(speed):
    ball_turtle.speed(speed)
    ball_turtle.penup()
    ball_turtle.goto(0, -200)
    ball_turtle.pendown()
    ball_turtle.setheading(270)
    ball_turtle.goto(0, -350)

def curve(speed):
    ball_turtle.speed(speed)
    ball_turtle.penup()
    ball_turtle.goto(0, -200)
    ball_turtle.pendown()
    ball_turtle.setheading(270)
    ball_turtle.goto(0, -300)
    ball_turtle.circle(50, extent=90)
    pass
    


# Draw the baseball diamond
draw_baseball_diamond()
fastball(1)
curve(1)

# Close the turtle graphics window when clicked
screen.exitonclick()