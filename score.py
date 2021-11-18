from turtle import Turtle

font = ('Arial', 70, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.goto(x=-100, y=200)
        self.write(self.l_score, align='center', font=font)
        self.goto(x=100, y=200)
        self.write(self.r_score, align='center', font=font)

    def add_to_left_score(self):
        self.l_score += 1
        self.clear()
        self.update_score()

    def add_to_right_score(self):
        self.r_score += 1
        self.clear()
        self.update_score()
