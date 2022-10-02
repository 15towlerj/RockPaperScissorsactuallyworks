import random
# allows use of the random.choice command
again = 0
# sets variable for while loop, allowing multiple games to be played successively
while (again == 0):
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_action = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_action)


    if user_action == "rock":
        if computer_action == "rock":
            print("Draw, you both chose rock!")

        elif computer_action == "scissors":
            print("You won congratulations the computer chose scissors!")

        else:
            print("You lost you loser the computer chose paper")
    elif user_action == "paper":
        if computer_action == "paper":
            print("Draw, you both chose paper!")

        elif computer_action == "rock":
            print("You won congratulations the computer chose rock!")
        else:
            print("You lost you loser the computer chose scissors")
    elif user_action == "scissors":
        if computer_action == "scissors":
            print("Draw, you both chose scissors!")

        elif computer_action == "paper":
            print("You won congratulations the computer chose paper!")

        else:
            print("You lost you loser the computer chose rock")
    else:
        print ("That wasn't an option please try again and don't mock me")
    again = int(input("Would you like to play the game again? Enter 0 for yes or 1 for no?"))
print ("Thanks for playing!")



