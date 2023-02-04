from turtle import Turtle


class CheckState():
    def __init__(self,):
        ...

    def check_state(self, go):
        new_check = Turtle()
        new_check.penup()
        new_check.shapesize(1, 1, 1)
        new_check.color('white')
        new_check.shape('circle')
        new_check.goto(go)
