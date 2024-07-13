import argparse
import sys
from closure_rps import main as rps
from guess import main as guessing

def choose(name = 'PlayerOne'):
    while True:
        print(f"{name} Welcome to the Arcade!")
        print(f"Choose\n" + "Rock, Paper ,Scissor".ljust(30 , '-') + '> 1\n' )
        print(f"Guess the number".ljust(30 , '-') + '> 2\n')
        print(f"Exit".ljust(30 , '-') + '> "x"' + '\n')

        game_choice = str(input("\nEnter:"))

        if game_choice == '1':
            fun1 = rps(name)
            fun1()
            # return choose(name)

            
        elif game_choice == '2':
            fun2 = guessing(name)
            fun2()
            # return choose(name)

        else :
            sys.exit("Thanks for playing".center(50 , '*').upper() + '\n\n')
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description = 'Welcome to Arcade'
    )

    parser.add_argument('-n' , '--name' , metavar = 'name' , required = True , help = "Please enter your name to enter Arcade")

    args = parser.parse_args()
    choose(args.name)