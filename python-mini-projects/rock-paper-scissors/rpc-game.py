import random

class Player:
    def choose(self):
        choice = input('enter your choice(snag/kaghaz/gheychi): ').lower
        return choice

class Computer:
    def choose(self):
        return random.choice(["sang", "kaghaz", "gheychi"])
    
class Game:
    def conditioanl(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "Tied!"

        elif player_choice == "sang" and computer_choice == "kaghaz":
            return "computer win"

        elif player_choice == "sang" and computer_choice == "gheychi":
            return "player win"

        elif player_choice == "kaghaz" and computer_choice == "gheychi":
            return "computer win"

        elif player_choice == "kaghaz" and computer_choice == "sang":
            return "player win"

        elif player_choice == "gheychi" and computer_choice == "sang":
            return "computer win"

        elif player_choice == "gheychi" and computer_choice == "kaghaz":
            return "computer win"


def start(self):
    print('game started!')
    player_choice = self.player.choose()
    computer_choice = self.computer.choose()
    print(f"entekhabe computer: {computer_choice}")
    #TBA: result...                    
                
                

            
        
