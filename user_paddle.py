from paddle import Paddle

x_position = -350
y_position = 0


class UserPaddle(Paddle):
    def __init__(self):
        super().__init__()
        self.goto(x=x_position, y=y_position)

    def go_up(self):
        new_y_position = self.ycor() + 10
        self.goto(x=self.xcor(), y=new_y_position)

    def go_down(self):
        new_y_position = self.ycor() - 10
        self.goto(x=self.xcor(), y=new_y_position)
