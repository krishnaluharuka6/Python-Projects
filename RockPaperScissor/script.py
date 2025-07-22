import random

item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your move = Rock , Paper , Scissor \n").title()

computer_choice = random.choice(item_list)

print(f"You choice is {user_choice} \n Computer choice is {computer_choice}")

if user_choice == computer_choice:
    print("Both chose same: Match Tie")

elif user_choice == "Rock":
    if computer_choice == "Scissor":
        print("Yey! You won it")
    elif computer_choice == "Paper":
        print("Computer won the game")

elif user_choice == "Paper":
    if computer_choice == "Scissor":
        print("Computer won the game")
    elif computer_choice == "Rock":
        print("Yey! You won it")

elif user_choice == "Scissor":
    if computer_choice == "Rock":
        print("Computer won the game")
    elif computer_choice == "Paper":
        print("Yey! You won it")

else:
    print("Please enter your choice properly !")



