rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

rock_paper_scissors = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice < 0 or user_choice > 2:
    print("Invalid number! Try again!")
else:
    show_user_choice = rock_paper_scissors[user_choice]
    print(show_user_choice)
    computer_choice = random.randint(0, 2)
    show_computer_choice = rock_paper_scissors[computer_choice]
    print(show_computer_choice)
    if user_choice == computer_choice:
        print("It's a draw!")
    elif user_choice == 0 and computer_choice == 1:
        print("You lose!")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 1 and computer_choice == 0:
        print("You win!")
    elif user_choice == 1 and computer_choice == 2:
        print("You lose!")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose!")
    elif user_choice == 2 and computer_choice == 1:
        print("You win!")