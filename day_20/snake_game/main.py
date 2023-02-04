from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

score_board = ScoreBoard()

snake = Snake()
food = Food()


screen.listen()
screen.onkey(snake.moves_up, 'Up')
screen.onkey(snake.moves_down, 'Down')
screen.onkey(snake.moves_left, 'Left')
screen.onkey(snake.moves_right, 'Right')

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    # DETECT COLLISION WITH FOOD
    if snake.head.distance(food) < 15:
        food.refresh()
        print('eat  ')
        score_board.increase_score()
        snake.extend()

    # DETECT COLLISION WITH WALL
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.reset()
        snake.reset()

    # DETECT COLLISION WITH TAIL
    # if head collides with any sagment in the tail
    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            score_board.reset
            snake.reset()


screen.exitonclick()
