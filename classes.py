import random
from ascii_art import shield, sword, magic, hearts

class RockPaperScissors():
    def __init__(self) -> None:

        # health and choice variables for the game

        self.health = 3
        self.weapons = {
            'sword': 0,
            'shield': 1,
            'magic': 2
        }

    def cpu_choice(self) -> str:

        # random computer decisions
        # returns the chosen int

        return random.choice(list(self.weapons.keys()))

    def check_result(self, player_choice:int, cpu_choice:int) -> str:
        
        # this logic is from Thomas Ward on stack.exchange
        # determines if the player loses, ties or wins

        if outcome == 0:
            print('You both selected the same weapon. Tie!')
            print()
        elif outcome == 1:
            print('You have triumphed over the enemy. Victory!')
            print()
        elif outcome == 2:
            print('You have been vanquised by the enemy. Defeat. (-1 life.)')
            self.health -= 1
            print()

    def graphics(self, player_choice:str, cpu_choice:str) ->str:
 
        # draws the ascii art depending on cpu and player choice.

        if player_choice == 'sword':
            sword()
        elif player_choice == 'shield':
            shield()
        elif player_choice == 'magic':
            magic()

        print('           VS')
        
        if cpu_choice == 'sword':
            sword()
        elif cpu_choice == 'shield':
            shield()
        elif cpu_choice == 'magic':
            magic()

    def run_game(self) ->str:

        # the game code. takes the instance methods and puts them together to create a game

        while True:
            print(f'You have {self.health} lives remaining')
            print()
            print('Sword: Outspeeds magic but is blocked by a shield')
            print('Shield: Blocks swords but not magic')
            print('Magic: Goes through shields but is outsped by a sword')
            print()

            player_choice = input('What weapon will you chose?: ').lower()
            print()
            print('-----------------------------------------------')
            print()

            if player_choice not in self.weapons.keys():
                print('Thats not a valid choice! Choose again.')
                print()
            else:
                break
            
        cpu_choice = self.cpu_choice()

        self.graphics(player_choice, cpu_choice)

        print(f'You have selected {player_choice}, the enemy has selected {cpu_choice}.')
        print()
        print('-----------------------------------------------')
        print()

        self.check_result(self.weapons[player_choice], self.weapons[cpu_choice])
