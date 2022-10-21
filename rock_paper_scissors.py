import random

def rock_paper_scissors():
    player_score = 0
    computer_score = 0
    while True:
        choices = ['rock', 'paper', 'scissors']
        player_choice = input("Let's play rock, paper, scissors! Enter 'rock'/'paper'/'scissors' or 'quit' to quit: ")
        computer_choice = random.choice(choices)
        if player_choice.lower().strip() == computer_choice:
            print(f"Computer chose: {computer_choice}")
            print("Game Tied!")
        elif player_choice.lower().strip() == 'rock':
            if computer_choice == 'paper':
                print("Computer chose: paper")
                print("You lose!")
                computer_score += 1
            else:
                print("Computer chose: scissors")
                print("You win!")
                player_score += 1
        elif player_choice.lower().strip() == 'paper':
            if computer_choice == 'scissors':
                print("Computer chose: scissors")
                print("You lose!")
                computer_score += 1
            else:
                print("Computer chose: rock")
                print("You win!")
                player_score += 1
        elif player_choice.lower().strip() == 'scissors':
            if computer_choice == 'rock':
                print("Computer chose: rock")
                print("You lose!")
                computer_score += 1
            else:
                print("Computer chose: paper")
                print("You win!")
                player_score += 1
        elif player_choice.lower().strip() == 'quit':
            print("Here is the final score:")
            print(f"Player score: {player_score}")
            print(f"Computer score: {computer_score}")
            print("Thanks for playing!")
            break
        else:
            print("Not a valid selection. Please enter 'rock'/'paper'/'scissors' or 'quit' to quit.")
        
rock_paper_scissors()