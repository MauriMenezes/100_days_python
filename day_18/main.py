import turtle as t
from random import choice, randint

turtle = t.Turtle()

t.colormode(255)
# for _ in range(4):

#     turtle.fd(10)
#     turtle.penup()
#     turtle.fd(10)
#     turtle.pendown()

colors = ['medium violet red', 'medium spring green', 'yellow']


# def draw_shape(num_sides):

#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         turtle.fd(100)
#         turtle.right(angle)


# for shape_side in range(4, 11):
#     turtle.color(choice(colors))
#     draw_shape(shape_side)


sides = [0, 90, 180, 270]
turtle.pensize(0.5)
turtle.speed('fastest')


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color


# for _ in range(200):
#     tup = random_color()
#     turtle.pencolor(tup)
#     turtle.fd(30)
#     turtle.setheading(choice(sides))


def draw_circle(gap):
    for i in range(0, 360, gap):
        tup = random_color()
        turtle.pencolor(tup)
        turtle.setheading(i)
        print(turtle.heading())
        turtle.circle(100)


draw_circle(1)

screen = t.Screen()
screen.exitonclick()
