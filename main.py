from turtle import Screen
from computer_paddle import ComputerPaddle
from user_paddle import UserPaddle
from ball import Ball
import time

screen = Screen()
screen.tracer(0)
screen.title('Pong')
screen.bgcolor('black')
screen.setup(width=800, height=600)

cpu_paddle = ComputerPaddle()
user_paddle = UserPaddle()

ball = Ball()

screen.listen()
screen.onkey(user_paddle.go_up, 'w')
screen.onkey(user_paddle.go_down, 's')
screen.onkey(cpu_paddle.go_up, 'Up')
screen.onkey(cpu_paddle.go_down, 'Down')

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with left paddle
    elif ball.xcor() > -340 and ball.distance(user_paddle) < 40:
        ball.bounce_x()

    # detect collision with right paddle
    elif ball.xcor() > 340 and ball.distance(cpu_paddle) < 40:
        ball.bounce_x()


screen.exitonclick()
