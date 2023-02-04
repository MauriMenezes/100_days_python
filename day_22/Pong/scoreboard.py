from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_l = 0
        self.score_r = 0
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.write_score()
        self.hideturtle()

    def write_score(self):
        self.clear()
        self.write(f' {self.score_l} | {self.score_r}',
                   align=ALIGNMENT, font=FONT)

    def l_scores(self):
        self.score_l += 1
        self.write_score()

    def r_scores(self):
        self.score_r += 1
        self.write_score()
