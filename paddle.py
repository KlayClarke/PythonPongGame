from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.speed('fastest')
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=0.5, outline=None)
        self.color('white')

    def go_up(self):
        new_y_position = self.ycor() + 10
        self.goto(x=self.xcor(), y=new_y_position)

    def go_down(self):
        new_y_position = self.ycor() - 10
        self.goto(x=self.xcor(), y=new_y_position)
