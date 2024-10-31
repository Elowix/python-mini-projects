# TBA: limitation for output

import random  

length = int(input('Enter the character password length: '))  

letter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"  
num = '1234567890'  
symbols = '!@#$%^&*()_+=-'  

all_characters = letter + num + symbols  

password = ''  

for i in range(length):  
    password += random.choice(all_characters)

print(password)
