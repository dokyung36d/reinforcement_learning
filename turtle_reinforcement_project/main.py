import turtle
from environment import draw_baseball_diamond, bat
from ball import fastball, curve, fastball_trajectory, curve_trajectory
from defender import *
import math
from reinforcement.env import *
from reinforcement.env import  Pitcher

#from hit import hit_ball



def simulation(timing, pitcher : Pitcher, env : Environment):
    assert isinstance(env, Environment)
    # screen = turtle.Screen()
    # screen.setup(width=1000, height=800)

    draw_baseball_diamond()
    #bat(1)
    set_location_turtle(turtle_list)

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
    bat_turtle.speed(1000)
    bat_turtle.shapesize(stretch_wid=0.5, stretch_len=6, outline=1)
    bat_turtle.penup()
    bat_turtle.goto(0, -350)


    #0~150까지 설정 가능(Int)
    start_time = timing

    trajectory = pitcher.return_trajectory(env)

    if trajectory == "fastball":
        for i in range(0, len(fast_traj[0]), 5): #총 150
            if i == 1:
                ball_turtle.pendown()
            ball_turtle.goto(fast_traj[0][i], curve_traj[1][i])

            if i >= start_time:
                plus_angle = i - start_time
                total_angle = (270 + plus_angle * 6/5) % 360
                bat_turtle.setheading(total_angle)

    else:
        for i in range(0, len(fast_traj[0]), 5): #총 150
            if i == 1:
                ball_turtle.pendown()
            ball_turtle.goto(curve_traj[0][i], curve_traj[1][i])

            if i >= start_time:
                plus_angle = i - start_time
                total_angle = (270 + plus_angle * 6/5) % 360
                bat_turtle.setheading(total_angle)
        bat_turtle.speed(100)
        ball_turtle.setheading(270)
    #ball_turtle의 y좌표가 -350일 때
    ball_x, ball_y = ball_turtle.position()
    if ball_y == -350 and ball_x == 0:
        if 270<=total_angle<=360:
            # print(total_angle)
            angle = 360 - total_angle
            ball_turtle.setheading(90-angle)
            ball_turtle.speed(50)

        else:
            # print(total_angle)
            angle = 360 - total_angle
            ball_turtle.setheading(90-angle)
            ball_turtle.speed(50)
            # ball_turtle.forward(5000)

    flag = 0
    
    ball_turtle.speed(1000)
    for i in range(25):
        ball_turtle.forward(30)
        current_x, current_y = ball_turtle.xcor(), ball_turtle.ycor()

        for j in range(len(defender_locations)):
            distance = math.sqrt((current_x - defender_locations[j][0]) ** 2 + (current_y - defender_locations[j][1]) ** 2)

            if distance <= 13:
                return "out"
                flag = 1
                break
        if flag == 1:
            break

    if flag == 1:
        result = "out"

    elif (start_time<0 or start_time > 150) and trajectory == "fastball":
        result = "strike"

    elif (start_time<0 or start_time > 150) and trajectory == "curve":
        result = "ball"
    #파울인 경우 45~90, 270~315

    elif (0<start_time<150) and trajectory == "curve":
        result = "strike"

    elif 45 < total_angle < 90 or 270 < total_angle < 315: #왼쪽 오른쪽, 중심은 0도
        result = "Foul"

    elif 0 < total_angle < 11.25 or 348.75 < total_angle < 360:
        result = "homerun"

    elif 11.25 < total_angle < 22.5 or 337.5 < total_angle < 348.75:
        result = "triple"

    elif 22.5 < total_angle < 33.75 or 326.25 < total_angle < 337.5:
        result = "double"

    elif 33.75 < total_angle < 45 or 315 < total_angle < 326.25:
        result = "single"
    # bat_turtle.shape("circle")
    # bat_turtle.color("white")
    bat_turtle.shapesize(stretch_wid=0.001, stretch_len=0.001, outline=0.001)

    return result



# for i in range(len(fast_traj[0])):
#     if i == 1:
#         ball_turtle.pendown()
#     ball_turtle.goto(curve_traj[0][i], curve_traj[1][i])