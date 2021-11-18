from classes import RockPaperScissors
# imports my game class

from ascii_art import shield, sword, magic, game_over, hearts

if __name__ == '__main__':
    # assigns a varaible to the game class
    game = RockPaperScissors()

    while True:
        # calls the instance method in the class to run the game
        game.run_game()

        while True:
            # monitors the player's health and determines when the game ends
            if game.health == 0:
                print('-----------------------------------------------')
                print('Out of lives.')
                game_over()
                print()
                exit()
            else:
                break
