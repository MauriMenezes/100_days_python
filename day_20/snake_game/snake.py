from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle('square')
        segment.color('white')
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def reset(self):
        for i in self.segments:
            i.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())
        # add a new segment to the snake
        ...

    # MOVES THE LAST SEGMENT TO THE NEXT POSITION UNTIL REACH THE 1°

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i-1].xcor()
            new_y = self.segments[i-1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.segments[0].fd(MOVE_DISTANCE)

    def moves_up(self):
        if self.segments[0].heading() != DOWN:
            self.head.setheading(UP)

    def moves_down(self):
        if self.segments[0].heading() != UP:
            self.head.setheading(DOWN)

    def moves_right(self):
        if self.segments[0].heading() != LEFT:
            self.head.setheading(RIGHT)

    def moves_left(self):
        if self.segments[0].heading() != RIGHT:
            self.head.setheading(LEFT)

    # MOVES THE SECOND SEGMENTS TO THE 1° POSITION

    # def different_move(self):
    #     for i in range(len(self.segments)):
    #         current_segment_x = self.segments[i].xcor()
    #         current_segment_y = self.segments[i].ycor()
    #         self.segments[i-1].goto(current_segment_x, current_segment_y)
    #     self.segments[0].fd(MOVE_DISTANCE)
    #     print(i)
