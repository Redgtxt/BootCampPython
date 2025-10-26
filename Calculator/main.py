import string
import os
calculator_ascii = """
 _____________________
|  _________________  |
| |  1234567890   | | |
| |_______________| | |
|  ___ ___ ___ ___  |
| | 7 | 8 | 9 | + | |
| |___|___|___|___| |
| | 4 | 5 | 6 | - | |
| |___|___|___|___| |
| | 1 | 2 | 3 | x | |
| |___|___|___|___| |
| | . | 0 | = | / | |
| |___|___|___|___| |
|___________________|
"""

def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

def calculate(first_number,second_number,sign):
    if(sign == "+"):
        return soma(first_number,second_number)
    elif(sign == "-"):
        return subtrai(first_number,second_number)
    elif(sign == "x"):
        return multiplica(first_number,second_number)
    elif(sign == "/"):
        return divide(first_number,second_number)

useResult = False
result = 0

print(calculator_ascii)
while(1):
    if not useResult:
        first_number = int(input("What's the first number?: "))
        result = first_number
    print("+")
    print("-")
    print("x")
    print("/")
    sign = input("Pick an operation: ")
    second_number = int(input("What's the next number?: ")) 
    result = calculate(result,second_number,sign)
    question = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:\n")

    if(question == "y"):
        useResult = True
    else:
        useResult = False
        os.system("clear")

