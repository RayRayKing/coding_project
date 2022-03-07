import turtle
import pandas

FONT = ("Arial", 8, "normal")

CSV = "50_states.csv"
screen = turtle.Screen()
screen.title("US QUIZ GAME")
image = "blank_states_img.gif"
screen.addshape(image)


def create_state():
    state = turtle.Turtle()
    state_data = data[data.state == answer_state]
    state_name = state_data.state
    state_x = int(state_data.x)
    state_y = int(state_data.y)
    state.penup()
    state.hideturtle()
    state.goto(x=state_x, y=state_y)
    state.write(answer_state, align="center", font=FONT)




turtle.shape(image)
# Read CSV
data = pandas.read_csv(CSV)
dict_data = data.to_dict()
state_list = data["state"].to_list()

game_on = True
Score = 0
while game_on:
    answer_state = screen.textinput(f"{Score}/{len(state_list)} Guess the State", "Name a state!").title()
    if answer_state in state_list:
        create_state()
        Score += 1
    elif answer_state is None:
        game_on = False
    elif Score == len(state_list):
        game_on = False
        print("You Got it All!")
screen.exitonclick()

