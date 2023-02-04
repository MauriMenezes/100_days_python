from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color('white')
        self.x_move = 10
        self.y_move = 10
        self.inicial_position = (0, 0)
        self.move_speed = 0.1

        # self.speed('fastest')

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        print(f'{new_x=}')
        print(f'{new_y=}')
        self.goto(new_x, new_y)

    def bouce_y(self):
        self.y_move *= -1

    def bouce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def refresh(self):
        self.goto(self.inicial_position)
        self.move_speed = 0.1

        self.bouce_x()
