from turtle import Turtle

font = ('Arial', 16, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0

    def display_score(self):
        self.write(arg=f'{self.score}', move=False, align='center', font=font, )
