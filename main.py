#Rock - Paper - Scissors Game
#Author: Ayodeji Farominiyi
#Username: Mathefaro

import random
from enum import Enum

pos_options = ["R", "P", "S"]
#A class go give a name to the choices' attributes
class Action(Enum):
    Rock = "R"
    Paper = "P"
    Scissors = "S"

#A function to get the user's choice
def get_user_selection():
    u_choice = input("Enter a choice ('R' for rock, 'P' for paper or 'S' for scissors): ")
    action = Action(u_choice.upper())
    return action

#A function to get the computer's choice
def get_PC_selection():
    C_choice = random.choice(pos_options)
    action = Action(C_choice.upper())
    return action

#Using a loop so that the game can repeat if it results in a tie
while True:
    try:
        user_choice = get_user_selection()
        if user_choice in pos_options:
            pass
    except:
        print('\nIncorrect input, try again')
        continue

    CPU_choice = get_PC_selection()
    print(f"\n Player ({user_choice.name}): CPU ({CPU_choice.name}).\n")

    if user_choice == CPU_choice:
        print(f"Both players selected {user_choice.name}. It's a tie! So we go again.")
    elif user_choice == Action.Rock:
        if CPU_choice == Action.Scissors:
            print("User wins!")
            break
        else:
            print("CPU wins.")
            break
    elif user_choice == Action.Paper:
        if CPU_choice == Action.Rock:
            print("User wins!")
            break
        else:
            print("CPU wins.")
            break
    elif user_choice == Action.Scissors:
        if CPU_choice == Action.Paper:
            print(" User wins!")
            break
        else:
            print("CPU wins.")
            break
