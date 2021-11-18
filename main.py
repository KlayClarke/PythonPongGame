from turtle import Turtle, Screen
from computer_paddle import ComputerPaddle
from user_paddle import UserPaddle
from ball import Ball

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
    screen.update()
    ball.move()

screen.exitonclick()
