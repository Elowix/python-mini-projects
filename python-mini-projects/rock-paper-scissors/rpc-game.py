# class player tarif mikonim + kole kar haee ke bayad bokone(inpute...)
# class computer baraye kolle kar haee ke computer bayad bokone(entekhab(s,k,gh))

# class moghayese baraye shart ha va taein kardane iinke dar che soorat yek plr barande hast
# def start barate tmamiye chiz haee ke bayad print beshan va mohasebati ke faghat marboot be khorooje hastan

# TBA (Conditionals...)
# (["Rock", "Paper", "scissors"])


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
                
                

            
        