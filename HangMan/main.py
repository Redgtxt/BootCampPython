import string
import random
from hangman_art import hangman_stages,logo
from words import word_list

lives = 7
animacao = 0
chosen_word = random.choice(word_list)
placeholder = "_" * len(chosen_word)
guessed_letters = []  # lista para guardar as letras já usadas

print(logo)
while lives > 0:
    print(f"Total of Lives: {lives}")
    if(animacao >= 0 and animacao  <= 6):
        print(hangman_stages[animacao])
    print(f"Word: {placeholder}")
    guess = input("Guess the Letter: ").lower()
    
    # Verifica se a letra já foi usada
    if guess in guessed_letters:
        print(f"Already guested '{guess}'. Try Again!")
        continue
    
    guessed_letters.append(guess)  # adiciona a letra à lista
    
    new_placeholder = ""

    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            new_placeholder += guess
        else:
            new_placeholder += placeholder[position]

    placeholder = new_placeholder  # atualiza com o novo progresso

    if chosen_word.find(guess) == -1:
        animacao += 1
        lives -= 1
        print(f"You guessed {guess},that's not in the word.You lose one life")
    else:
        print(f"You guessed {guess},that's in the word. Good job!")
    
    if(placeholder == chosen_word):
        break

if(0 >= lives):
    print("***********YOU LOST***********")
    print(f"The word was {chosen_word}")
else:
    print("***********YOU WIN***********")







