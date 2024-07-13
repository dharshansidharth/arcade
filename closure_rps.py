# the main motive of closure is to avoid global variables as it can be misused

import sys
import random
from enum import Enum
import argparse

print("")
print("player1".upper().center(30 , "*") + '\n\n')

def main(name):
    class rps(Enum):
        stone = 1
        paper = 2
        scissor = 3
        
    gamecount = 0
    player1_score = 0
    player2_score = 0

    def play():
        nonlocal name
        nonlocal player1_score , player2_score
        choice1 = int(
            input(f"\nDear {name} please, enter".center(30 , '-').upper() + '\n'
                # "  Enter  ".center(20 , '$').upper() + '\n\n'
                "stone".ljust(15 , '-') + '>' +  '1' + '\n'
                "Paper".ljust(15 , '-') + '>' + '2' +'\n'
                "Scissors".ljust(15 , '-') + '>' + '3' + '\n'
                "Exit".ljust(15 , '-') + '>' + '0' + '\n'
            )
        )
        nonlocal gamecount

        print("")
        # print("player2".upper().center(30 , "*"))
        choice2 = int(random.choice("123"))
        
        def winner(choice1 , choice2):
            nonlocal name
            nonlocal player2_score , player1_score
            nonlocal gamecount

            if choice1 == 0:
                print(f"\n\n Thanks {name} for playing".center(40 , '-') + "\n\n")
                return 

            elif choice1 > 3 or choice1 < 1:
                print(f"\nDear {name} please enter a valid option!\n")
                return play()

            elif (choice1 == choice2) :
                print("\n\n" + f" Match Drawn".center(20 , "*") + "\n\n")

            elif ((choice1 == 1 and choice2 == 2) or (choice1 == 2 and choice2 == 3) or (choice1 == 3 and choice2 == 1)):
                player2_score += 1
                print("Computer Wins! ".center(30 , '*'))
                print(f"\nComputer Choice {str(rps(choice2)).replace('rps.' , '')}")
                print(f"\n{name}'s Choice {str(rps(choice1)).replace('rps.' , '')} \n\n")

            else:
                player1_score += 1
                print("You win".center(30 , '*'))
                print(f"\n{name}'s Choice " + str(rps(choice1)).replace('rps.' , ''))
                print("\nComputer Choice " + str(rps(choice2)).replace('rps.' , '') + "\n\n")
        if choice1 >= 1 and choice1 <= 3:
            gamecount += 1

        winner(choice1 , choice2)
        print(f"{name}".upper().ljust(10 , '-') + "Computer".upper().rjust(10 , '-'))

        print(str(player1_score).ljust(10) + str(player2_score).rjust(10))

        print("\nGame Count = " + str(gamecount) + ' \n')
        if choice1 == 0 :
            print(f"Thanks for playing {name} ".center(40 , '*')) 
            return   
        return play()
        
        # if choice1 != 0:
        #     return play()
        # winner(choice1 , choice2)

    return play 


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description = 'Welcome to the game of rock paper scissors!'
    )

    parser.add_argument('-n' , "--name" , metavar = 'name' , required = True , help = "Give your name to play game")

    args = parser.parse_args()
    print(f" \nWelcome {args.name}\n ".center(50 , "*"))
    game = main(args.name)
    game()
