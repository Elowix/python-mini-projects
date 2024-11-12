# import random

# class Player:
#     def choose(self):
#         choice = input('enter your choice(rock/paper/scissors): ').lower
#         return choice

# class Computer:
#     def choose(self):
#         return random.choice(["rock", "paper", "scissors"])
    
# class Game:
#     def conditioanl(self, player_choice, computer_choice):
#         if player_choice == computer_choice:
#             return "tied!"

#         elif player_choice == "rock" and computer_choice == "paper":
#             return "computer win"

#         elif player_choice == "rock" and computer_choice == "scissors":
#             return "player win"

#         elif player_choice == "paper" and computer_choice == "gheychi":
#             return "computer win"

#         elif player_choice == "paper" and computer_choice == "rock":
#             return "player win"

#         elif player_choice == "scissors" and computer_choice == "rock":
#             return "computer win"

#         elif player_choice == "scissors" and computer_choice == "paper":
#             return "computer win"


#     def start(self):
#         print('game started!')
#         player_choice = self.player.choose()
#         computer_choice = self.computer.choose()
#         print(f"computer choose: {computer_choice}")
#         result = self.conditioanl(player_choice, computer_choice)
#         print(result)


# if __name__ == "__main__":  
#     game = Game()  
#     game.player = Player()  
#     game.computer = Computer()  
#     game.start()  



import random  

def compare(userg, pcg):  
    global user_joon, pc_joon  

    if userg == pcg:  
        return 'mosavi'  
    elif userg == 'sang' and pcg == "kaghaz":  
        pc_joon += 1  
        return 'pc barande shod!'  
    elif userg == 'sang' and pcg == "gheychi":  
        user_joon += 1  
        return 'user barande shod!'  
    elif userg == 'kaghaz' and pcg == "sang":  
        user_joon += 1  
        return 'user barande shod!'  
    elif userg == 'kaghaz' and pcg == "gheychi":  
        pc_joon += 1  
        return 'pc barande shod!'  
    elif userg == 'gheychi' and pcg == "sang":  
        pc_joon += 1  
        return 'pc barande shod!'  
    elif userg == 'gheychi' and pcg == "kaghaz":  
        user_joon += 1  
        return 'user barande shod!'  

match = int(input('chand dast mikhay bazi koni?: '))  

pc_joon = 0  
user_joon = 0  

for i in range(match):  
    userg = input('sang / kaghaz / gheychi: ')  
    
    skgh = ['sang', 'kaghaz', 'gheychi']  
    pcg = random.choice(skgh)  
    print(f'pc choice: {pcg}')  
    
    result = compare(userg, pcg) # Call the function here  

# Print final scores  
print(f'user rank: {user_joon}')  
print(f'pc rank: {pc_joon}')  

# Final output based on the result  
if result == 'pc barande shod!':  
    print('pc barande shod!')  
elif result == 'user barande shod!':  
    print('user barande shod!')  
elif user_joon == pc_joon:  
    print('mosavi!')  
elif user_joon > pc_joon:  
    print('user barande shod!')  
else:  
    print('pc barande shod!')        





    





