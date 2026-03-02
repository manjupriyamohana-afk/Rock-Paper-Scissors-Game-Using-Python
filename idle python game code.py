import random

def get_computer_choice():
    options = ["rock", "paper", "scissors"]
    return random.choice(options)

def decide_winner(user, computer):
    if user == computer:
        return "Tie"
    elif user == "rock" and computer == "scissors":
        return "User"
    elif user == "paper" and computer == "rock":
        return "User"
    elif user == "scissors" and computer == "paper":
        return "User"
    else:
        return "Computer"

def play_game():
    print("Rock Paper Scissors Game :")
    
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    computer_choice = get_computer_choice()
    
    print("Computer chose:", computer_choice)
    
    result = decide_winner(user_choice, computer_choice)
    
    if result == "Tie":
        print("It's a tie!")
    elif result == "User":
        print("You win!")
    else:
        print("Computer wins!")

play_game()
