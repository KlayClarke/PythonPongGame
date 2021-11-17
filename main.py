from turtle import Turtle, Screen
from computer_paddle import ComputerPaddle
from user_paddle import UserPaddle


game_on = True

cpu_paddle = ComputerPaddle()
user_paddle = UserPaddle()

print(user_paddle.xcor())
print(user_paddle.ycor())

screen = Screen()
screen.listen()
screen.onkey(user_paddle.go_up, 'Up')
screen.onkey(user_paddle.go_down, 'Down')
screen.title('Pong')
screen.bgcolor('black')
screen.setup(width=800, height=600)

while game_on:
    screen.update()


screen.exitonclick()
