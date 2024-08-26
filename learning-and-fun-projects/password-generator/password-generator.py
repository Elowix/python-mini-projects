import random

length = int(input('Enter the chracter password:'))

letter = "abcdefghijklmnopqrstuvxyzQWERTYUIOPLKJHGFDSAZXCVBNM"
num = '1234567890'
symbels = '!@#$%^&*()_+=-'
sums = len(letter) + len(num) + len(symbels)
all_character = letter + num + symbels

password = ''

for i in range(length):
    x = all_character[random.randint(0, sums)]
    password = password + x

print(password)




