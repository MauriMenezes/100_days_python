from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

colors = ['red', 'blue', 'yellow', 'purple', 'orange']

user_guess = screen.textinput(
    title='Make your bet', prompt='which turtle will win the race? Enter a color')
is_race_on = False
turtles = []
x_value = -230
y_value = -100

chegada = Turtle()
chegada.penup()
chegada.goto(x=200, y=200)
chegada.pendown()
chegada.right(90)
chegada.goto(x=200, y=-200)

for i in range(len(colors)):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[i])
    turtles.append(new_turtle)
    new_turtle.goto(x=x_value, y=y_value)
    y_value += 60

if user_guess:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 180:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_guess:
                print("You've won !")
            else:
                print("You've lost! ")
        random_distance = random.randint(1, 10)
        turtle.fd(random_distance)

screen.exitonclick()
