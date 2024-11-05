import random

class Player:
    def choose(self):
        choice = input('enter your choice(rock/paper/scissors): ').lower
        return choice

class Computer:
    def choose(self):
        return random.choice(["rock", "paper", "scissors"])
    
class Game:
    def conditioanl(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "tied!"

        elif player_choice == "rock" and computer_choice == "paper":
            return "computer win"

        elif player_choice == "rock" and computer_choice == "scissors":
            return "player win"

        elif player_choice == "paper" and computer_choice == "gheychi":
            return "computer win"

        elif player_choice == "paper" and computer_choice == "rock":
            return "player win"

        elif player_choice == "scissors" and computer_choice == "rock":
            return "computer win"

        elif player_choice == "scissors" and computer_choice == "paper":
            return "computer win"


    def start(self):
        print('game started!')
        player_choice = self.player.choose()
        computer_choice = self.computer.choose()
        print(f"computer choose: {computer_choice}")
        result = self.conditioanl(player_choice, computer_choice)
        print(result)


if __name__ == "__main__":  
    game = Game()  
    game.player = Player()  
    game.computer = Computer()  
    game.start()  
