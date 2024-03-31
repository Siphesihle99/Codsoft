import random

print("Rock-Paper-Scissors Game")

choices = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0
game_rounds = 0

def get_user_selection():
    print("1. Rock\n2. Paper\n3. Scissors")
    user_choice = int(input("Select your choice between(1,2, or 3) to start:"))
    return user_choice

def get_computer_selection():
    selection = random.randint(1, 3)
    return selection

def generate_winner(user_selection, computer_selection):
    if user_selection == computer_selection:
        return "it's a draw"
    elif user_selection == 1 and computer_selection == 3:
        return "you win!, Rock beats scissors"
    elif user_selection == 2 and computer_selection == 1:
        return "you win!, Paper beats rock"
    elif user_selection == 3 and computer_selection == 2:
        return "you win!, Scissors beats paper"
    else:
        return "you lose!"

def diplay(user_selection, computer_selection, result):
    print(f"you chose {choices[user_selection - 1]}, and computer chose {choices[computer_selection -1]}")
    print(result)

while True:
    game_rounds+=1
    user_selection = get_user_selection()
    computer_selection = get_computer_selection()
    outcome = generate_winner(user_selection, computer_selection)
    print(f"you chose {choices[user_selection - 1]}, and computer chose {choices[computer_selection -1]}")
    print(outcome)

    if "win" in outcome:
        user_score+=1
    elif "lose" in outcome:
        computer_score+=1
        
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thank you for playing")
        print(f"Your score is {user_score}, Computer score is {computer_score}, number of rounds is {game_rounds}")
        break
