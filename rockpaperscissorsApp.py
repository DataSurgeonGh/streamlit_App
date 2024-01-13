import streamlit as st
import random

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)_____
           _______)
          ________)
         _________)
---._____________)
"""

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

game_choices = [rock, paper, scissors]

def get_user_choice():
    user_choice = st.radio("What do you choose?", ["Rock", "Paper", "Scissors"])
    return ["Rock", "Paper", "Scissors"].index(user_choice)

def get_choice_name(choice):
    return ["Rock", "Paper", "Scissors"][choice]

def determine_winner(user_choice, machine_choice):
    if user_choice == machine_choice:
        return "Draw!"
    elif (user_choice == 0 and machine_choice == 2) or (user_choice == 2 and machine_choice == 1) or (user_choice == 1 and machine_choice == 0):
        return "You win!"
    else:
        return "You lose!"

def main():
    st.title("Rock, Paper, Scissors Game!")

    user_choice = get_user_choice()
    st.text(game_choices[user_choice])

    machine_choice = random.randint(0, 2)
    st.text(game_choices[machine_choice])

    result = determine_winner(user_choice, machine_choice)
    st.success(result)

if __name__ == "__main__":
    main()


# def main():
#     st.title("Rock, Paper, Scissors Game!")

#     user_choice = get_user_choice()
#     st.text(game_choices[user_choice], use_column_width=True)

#     machine_choice = random.randint(0, 2)
#     st.text(game_choices[machine_choice], use_column_width=True)

#     result = determine_winner(user_choice, machine_choice)
#     st.success(result)

# if __name__ == "__main__":
#     main()
