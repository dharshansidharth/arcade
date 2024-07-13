import sys
import argparse
import random

def main(name):
    gamecount = 0
    score = 0
    def play():
        nonlocal gamecount , name , score
        print(f"\n{name} can you guess what Iam thinking about 1 , 2 or 3...?\n")
        print("\n 'x' to exit\n")
        choice1 = str(input('Enter:'))
        choice2 = random.randint(1 , 3)
        def winner(choice1 , choice2):
            nonlocal name ,score
            if(choice1 == str(choice2)):
                score += 1
                print(f"\nYeah! you got it Iam thinking of the number {choice1}\n\n {name} you win!\n")
            elif int(choice1) < 0 or int(choice1) > 3:
                print(f"Dear {name} please enter 1 , 2 , 3 ...")
                return play()
            elif choice1 != 0:
                print(f"\nNo! Iam not thinking of the number {choice1}\n\n Iam thinking of the number {choice2} \n\n {name} you lose!\n")

        
        if choice1 != 'x':
            gamecount += 1
            winner(choice1 , choice2)
            print(f"\nGame count: {gamecount}\n\n")
            print(f"\n{name}'s score : {score}")
            print(f"\nWinning Percentage: {(score/gamecount) * 100 :.2f}%\n\n")
            return play()
        else:
            print(" Thanks for playing ".center(50 , '*').upper() + '\n\n')
            return 


    return play




if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description = "Welcome to the game of guessing!"
    )

    parser.add_argument('-n' , '--name' , metavar = 'name' , required = True , help = "Please ente your name to play!")

    args = parser.parse_args()

    fun = main(args.name)
    fun()
