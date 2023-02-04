from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        with open('data.txt', mode='r') as file:
            high_score = int(file.read())
            self.high_score = high_score
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.write_score()
        self.hideturtle()

    def write_score(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}',
                   align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w')as file:
                file.write(f'{self.high_score}')
        self.score = 0
        self.write_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.write_score()
