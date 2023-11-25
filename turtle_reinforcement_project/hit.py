import turtle
from environment import bat_x, global_angle
from main import ball_turtle

#실제 해당 게임에서는 변화구이면 치는 것 불가능


def hit_ball():
    ball_x, ball_y = ball_turtle.position()
    if ball_y == -350 and ball_x == 0:
        if 270<=global_angle<=360:
            angle = global_angle - 270
            ball_turtle.setheading(90 - angle)
            ball_turtle.speed(2)

        else:
            ball_turtle.setheading(global_angle + 90)
            ball_turtle.speed(2)

    pass
    #ball의 y좌표가 0일 때의 배트의 각도를 구히여 다음 예상 각도를 구함