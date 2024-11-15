import random

nplr = int(input('chand nafarin?: '))
plrname_list = []

for i in range(nplr):
    plrname = input('esme bazikonan ra vared konid: ')
    plrname_list.append(plrname)


chplr = random.choice(plrname_list)
print(chplr)



#tba....