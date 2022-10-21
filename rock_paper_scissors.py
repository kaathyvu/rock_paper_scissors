import random

def battle_of_the_elements():
    player_score = 0
    computer_score = 0
    while True:
        choices = ['wood', 'earth', 'water', 'fire', 'metal']
        player_choice = input("Let's play Battle of the Elements! Enter 'wood'/'earth'/'water'/'fire'/'metal' or 'quit' to quit: ")
        computer_choice = random.choice(choices)
        if player_choice.lower().strip() == computer_choice:
            print(f"Computer chose: {computer_choice}")
            print("Game Tied!")

        elif player_choice.lower().strip() == 'wood':
            if computer_choice == 'metal':
                print("Computer chose: metal")
                print("Metal chops wood, You lose!")
                computer_score += 1
            elif computer_choice == 'fire':
                print("Computer chose: fire")
                print("Fire burns wood, You lose!")
                computer_score += 1
            elif computer_choice == 'earth' :
                print("Computer chose: earth")
                print("Wood parts earth, You win!")
                player_score += 1
            elif computer_choice == 'water' :
                print("Computer chose: water")
                print("Wood absorbs water, You win!")
                player_score += 1

        elif player_choice.lower().strip() == 'water':
            if computer_choice == 'earth':
                print("Computer chose: earth")
                print("Earth absorbs water, You lose!")
                computer_score += 1
            elif computer_choice == 'wood':
                print("Computer chose: wood")
                print("Wood absorbs water, You lose!")
                computer_score += 1
            elif computer_choice == 'fire' :
                print("Computer chose: fire")
                print("Water douses fire, You win!")
                player_score += 1
            elif computer_choice == 'metal' :
                print("Computer chose: metal")
                print("Water rusts metal, You win!")
                player_score += 1

        elif player_choice.lower().strip() == 'metal':
            if computer_choice == 'fire':
                print("Computer chose: fire")
                print("Fire melts metal, You lose!")
                computer_score += 1
            elif computer_choice == 'water':
                print("Computer chose: water")
                print("Water rusts metal, You lose!")
                computer_score += 1
            elif computer_choice == 'wood' :
                print("Computer chose: wood")
                print("Metal chops wood, You win!")
                player_score += 1
            elif computer_choice == 'earth' :
                print("Computer chose: earth")
                print("Metal carves earth, You win!")
                player_score += 1

        elif player_choice.lower().strip() == 'earth':
            if computer_choice == 'wood':
                print("Computer chose: wood")
                print("Wood parts earth. You lose!")
                computer_score += 1
            elif computer_choice == 'metal':
                print("Computer chose: metal")
                print("Metal carves earth. You lose!")
                computer_score += 1
            elif computer_choice == 'water':
                print("Computer chose: water")
                print("Earth absorbs water. You win!")
                player_score += 1
            elif computer_choice == 'fire':
                print("Computer chose: fire")
                print("Earth smothers fire. You win!")

        elif player_choice.lower().strip() == 'fire':
            if computer_choice == 'earth':
                print("Computer chose: earth")
                print("Earth smothers fire. You lose!")
                computer_score += 1
            elif computer_choice == 'water':
                print("Computer chose: water")
                print("Water douses fire. You lose!")
                computer_score += 1
            elif computer_choice == 'metal':
                print("Computer chose: metal")
                print("Fire melts metal. You win!")
                player_score += 1
            elif computer_choice == 'wood':
                print("Computer chose: wood")
                print("Fire burns wood. You win!")
                player_score += 1

        elif player_choice.lower().strip() == 'quit':
            print("Here is the final score:")
            print(f"Player score: {player_score}")
            print(f"Computer score: {computer_score}")
            print("Thanks for playing!")
            break
        else:
            print("Not a valid selection. Please enter 'wood'/'earth'/'water'/'fire'/'metal' or 'quit' to quit")

battle_of_the_elements()


