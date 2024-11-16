import random

chbr = int(input('How many winners do you want to have?: '))
if chbr == 0:
       print('0, you idiot!?')
       exit()


plrname = None
plrname_list = []
while plrname != 'end':
        plrname = input('Enter the name: ')

        if plrname == 'end':
                print('You have finished the lottery')
                break
        
        plrname_list.append(plrname)

        for plrname in plrname_list:
                 plrname_list.remove(plrname)
                 print('iin name ghablan boode')
    
        if plrname == '':
               plrname_list.remove('')
               print('input cannot be empty!')

        print(plrname_list)

for i in range(chbr):
    chplr = random.choice(plrname_list)
    print(f'Winner of lottery number {i+1}: {chplr}')







