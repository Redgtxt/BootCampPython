import random

def check_number(num,guess):
    
    if(num == guess):
        print("You guessed it!")
        return True
    
    if(num > guess):
        print("Higher")
    elif(guess > num):
        print("Lower")
    return False

def main_loop(lives):
        while(0 < lives):
            guess = int(input("Guess: "))
            if(check_number(num,guess)):
                break
            lives-= 1
            print(f"Tentativas atuais: {lives}")

num = random.randrange(1,101)
#print(f"Estou a chetar o {num}")
dificulty = input("Choose the difficulty 'easy' or 'hard' ").lower()
if(dificulty == "easy"):
    main_loop(10)
else:
    main_loop(5)

