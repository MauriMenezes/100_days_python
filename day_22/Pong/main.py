from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.title('PONG')
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)


screen.listen()
score_board = ScoreBoard()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # COLLISION WITH WALL
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bouce_y()

    # COLLISION WITH PADDLE
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bouce_x()
    # if the ball goes out
    if ball.xcor() > 400:
        score_board.r_scores()
        ball.refresh()
    if ball.xcor() < -380:
        score_board.l_scores()
        ball.refresh()


screen.exitonclick()
