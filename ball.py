from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize()
        self.penup()

    def move(self):
        new_x_position = self.xcor() + 1
        new_y_position = self.ycor() + .75
        self.goto(x=new_x_position, y=new_y_position)
