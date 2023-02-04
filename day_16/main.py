# from turtle import Turtle, Screen

# timmy = Turtle()

# timmy.shape('turtle')
# timmy.color('coral')
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
pokemons = ['Pikachu', 'Squirtle', 'Charmander']
types = ['Electric', 'Water', 'Fire']
table = PrettyTable()
table.add_column('Pokemon Name ', pokemons)
table.add_column('Type', types)

print(table)
