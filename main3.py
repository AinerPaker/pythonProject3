import random

def play():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    player_choice = input("Rock, paper, or scissors? ").lower()

    print("You chose " + player_choice + ", and the computer chose " + computer_choice + ".")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == 'rock':
        if computer_choice == 'paper':
            print("You lose!")
        else:
            print("You win!")
    elif player_choice == 'paper':
        if computer_choice == 'scissors':
            print("You lose!")
        else:
            print("You win!")
    elif player_choice == 'scissors':
        if computer_choice == 'rock':
            print("You lose!")
        else:
            print("You win!")
    else:
        print("Invalid input. Please choose either rock, paper, or scissors.")

    play_again = input("Do you want to play again? (y/n)").lower()
    if play_again == 'y':
        play()
    else:
        print("Thanks for playing!")

play()
