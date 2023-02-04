# import colorgram

# colors = colorgram.extract('hirstspots.jpg', 30)

# lista = []
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new_color = (r, g, b)
#     lista.append(new_color)
# print(lista)
import turtle as t
from random import choice, randint


turtle = t.Turtle()
t.colormode(255)


color_list = [(141, 176, 206), (25, 32, 48), (28, 105, 156), (208, 161, 112), (238, 222, 234), (230, 211, 94), (131, 31, 64), (5, 162, 195), (182, 45, 84), (217, 60, 85), (226, 80, 44), (195, 129, 168),
              (54, 167, 116), (29, 61, 115), (108, 181, 91), (109, 99, 88), (2, 102, 119), (193, 187, 47), (241, 204, 1), (19, 22, 21), (52, 149, 109), (171, 211, 173), (226, 170, 186), (150, 207, 222), (234, 169, 160), (184, 186, 210), (115, 38, 37)]
(240, 242, 246)

# turtle.fd(50)
# turtle.dot(20, "blue")
# turtle.fd(50)
# turtle.dot(20, "blue")
turtle.speed('fastest')
turtle.penup()
turtle.hideturtle()

turtle.setheading(205)
turtle.fd(300)
turtle.setheading(0)


def choice_random_color(lista):
    color = choice(lista)
    return color


qtd_dots = 100
for i in range(1, (qtd_dots+1)):
    turtle.dot(20, choice_random_color(color_list))
    turtle.fd(50)
    print(i)
    value = i % 10 == 0
    print(value)
    if value:
        turtle.setheading(90)
        turtle.fd(50)
        turtle.setheading(180)
        turtle.fd(500)
        turtle.setheading(0)


screen = t.Screen()
screen.exitonclick()
