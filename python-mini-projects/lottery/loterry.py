import random
import time

chbr = int(input('chand barande mikhay dashte bashi?: '))
if chbr == 0:
       print('0 dalghak!? ')
       time.sleep(2)


plrname = None
plrname_list = []
while plrname != 'end':
        plrname = input('esme ro vared kon: ')
        if plrname == 'end':
                print('shoma ghore ro be payan resondi')
        if chbr == 0:
                print('vayyyy! voroodi 0 dadi alan esmo vared mikoni ke chi besheee!')        
                break
        plrname_list.append(plrname)
        if plrname == '':
               plrname_list.remove('')
               print('voroodi nemitoone khali bashe!')

        print(plrname_list)

for i in range(chbr):
    chplr = random.choice(plrname_list)
    print(f'barande nafare {i+1} ghore: {chplr}')





