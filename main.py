from turtle import Screen
from right_paddle import RightPaddle
from left_paddle import LeftPaddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.tracer(0)
screen.title('Pong')
screen.bgcolor('black')
screen.setup(width=800, height=600)

left_paddle = LeftPaddle()
right_paddle = RightPaddle()

left_score = Score()
right_score = Score()

ball = Ball()

screen.listen()
screen.onkey(left_paddle.go_up, 'w')
screen.onkey(left_paddle.go_down, 's')
screen.onkey(right_paddle.go_up, 'Up')
screen.onkey(right_paddle.go_down, 'Down')

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with left paddle
    elif ball.xcor() > -340 and ball.distance(left_paddle) < 40:
        ball.bounce_x()

    # detect collision with right paddle
    elif ball.xcor() > 340 and ball.distance(right_paddle) < 40:
        ball.bounce_x()

    # detect the left paddle missing the ball - right paddle gains point
    elif ball.xcor() < -380:
        right_score.score += 1
        print(right_score.score)
        ball.reset_position()

    # detect the right paddle missing the ball - left paddle gains point
    elif ball.xcor() > 380:
        left_score.score += 1
        print(left_score.score)
        ball.reset_position()


screen.exitonclick()
