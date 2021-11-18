from paddle import Paddle

x_position = 350
y_position = 0


class RightPaddle(Paddle):
    def __init__(self):
        super().__init__()
        self.goto(x=x_position, y=y_position)
