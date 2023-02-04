from turtle import Turtle, Screen
from check_state import CheckState
import pandas

screen = Screen()
screen.title('U.S. States Games')
image = "gifs-do-mapa-do-brasil-4.gif"
screen.bgpic(image)
check = CheckState()

guessed_states = []


while len(guessed_states) < 27:
    data = pandas.read_csv('27_states.csv')
    answer_state = screen.textinput(
        title='Guess the state', prompt="what's another states name's ?").title()
    print(answer_state)
    state_list = data['state'].tolist()
    # print(state_list)

    if answer_state in state_list:
        guessed_states.append(answer_state)
        state = data[data['state'] == answer_state]
        x_state = int(state.x)
        y_state = int(state.y)
        print(x_state, y_state)
        check.check_state((x_state, y_state))

screen.exitonclick()
