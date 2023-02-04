import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player_1 = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.onkeypress(player_1.moves_up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_cars()

    # detect collision
    for i in car.cars:
        if i.distance(player_1) < 20:
            scoreboard.game_over()
            game_is_on = False
    # sucessfull cross
    if player_1.finish_line():
        player_1.go_to_start()
        car.level_up()
        scoreboard.increase_level()
