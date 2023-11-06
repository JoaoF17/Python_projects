from turtle import Turtle, Screen
from create_state import CreateState
import pandas as pd

screen = Screen()
screen.title("U.S States Game")
screen.bgpic('blank_states_img.gif')

#get data from csv
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()

create_state =  CreateState()

game_on = True
while game_on:
  #user input
  answer_state = screen.textinput(title=f"{create_state.number_of_states}/50 Guess the state", prompt="Write down a U.S state:").title()
  
  #display it on the screen
  if answer_state == "Exit":
    break
  elif answer_state in all_states:
    #format user input 
    guessed_state = data[data.state == answer_state]
    state_name = guessed_state["state"].item()
    state_x = int(guessed_state["x"].iloc[0])
    state_y = int(guessed_state["y"].iloc[0])
    create_state.state_found(state_name, state_x, state_y)
  elif create_state.number_of_states > 50:
    create_state.finish()


screen.exitonclick()