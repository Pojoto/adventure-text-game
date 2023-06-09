'''
Project 3 - Text Adventure - Spring 2023  
Author: John Lewis - lewis63

Modified by:  Joshua Gao (joshuagao)

The program presents a text-based adventure game with
multiple rooms and items.
'''

from game import Game
import os


def main():

    print(os.getcwd())

    game = Game()
    
    finished = False
    
    while not finished:
        print()
        command_input = input('> ')
        print()
        command = game.clean_command(command_input)
        if command == 'quit':
            finished = True
        else:
            game.process_command(command)    


# Call main like this to keep Web-CAT happy:
if __name__ == '__main__':
    main()
