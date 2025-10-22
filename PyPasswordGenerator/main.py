import string
import random

letters = list(string.ascii_letters)  # a-z + A-Z
numbers = list(string.digits)          # 0-9
symbols = list(string.punctuation)    # símbolos comuns

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters do you want your password to have "))
nr_numbers = int(input("How many numbers do you want your password to have "))
nr_symbols = int(input("How many symbols do you want your password to have "))

password = []

#Letters
for i in range(nr_letters):
    letra = random.choice(letters)
    password.append(letra)

#Symbols

for i in range(nr_symbols):
    symbol = random.choice(symbols)
    password.append(symbol)

#Numbers
for i in range(nr_numbers):
    number = random.choice(numbers)
    password.append(number)

random.shuffle(password)
final_password = "".join(password)


    
print(f"Your password is: {final_password}")