import turtle
from environment import draw_baseball_diamond, bat
from ball import fastball, curve, fastball_trajectory, curve_trajectory
#from hit import hit_ball

screen = turtle.Screen()
screen.setup(width=1000, height=800)

draw_baseball_diamond()
#bat(1)

ball_turtle = turtle.Turtle()
ball_turtle.shape("circle")

# fastball(1, ball_turtle)
# curve(1, ball_turtle)
#hit_ball()

#둘 중 random하게 정하면 될 듯
fast_traj = fastball_trajectory()
curve_traj = curve_trajectory()


#이전에 fastball인지 curve인지를 판단해야햠.
#직구 궤적과 curve 궤적을 미리 정의 -> 이후 
# while ball_turtle.position()[0] != 0:
#     pass
bat_turtle = turtle.Turtle()
bat_turtle.shape("square")
bat_turtle.shapesize(stretch_wid=0.5, stretch_len=6, outline=1)
bat_turtle.penup()
bat_turtle.goto(0, -350)

start_time = 30

for i in range(0, len(fast_traj[0]), 5): #총 150
    if i == 1:
        ball_turtle.pendown()
    ball_turtle.goto(fast_traj[0][i], curve_traj[1][i])

    if i >= start_time:
        plus_angle = i - start_time
        total_angle = (270 + plus_angle * 6/5) % 360
        bat_turtle.setheading(total_angle)

#ball_turtle의 y좌표가 -350일 때
ball_x, ball_y = ball_turtle.position()
if ball_y == -350 and ball_x == 0:
    if 270<=total_angle<=360:
        angle = 360 - total_angle
        ball_turtle.setheading(90-angle)
        ball_turtle.speed(5)
        ball_turtle.forward(5000)

    else:
        print(total_angle)
        angle = 360 - total_angle
        ball_turtle.setheading(90-angle)
        ball_turtle.speed(5)
        ball_turtle.forward(5000)





# for i in range(len(fast_traj[0])):
#     if i == 1:
#         ball_turtle.pendown()
#     ball_turtle.goto(curve_traj[0][i], curve_traj[1][i])
    

screen.exitonclick()