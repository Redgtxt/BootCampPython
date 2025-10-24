alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

banner = r"""
  ___    __    ____  ___    __    ____     ___  ____  ____  _   _  ____  ____ 
 / __)  /__\  ( ___)/ __)  /__\  (  _ \   / __)(_  _)(  _ \( )_( )( ___)(  _ \
( (__  /(__)\  )__) \__ \ /(__)\  )   /  ( (__  _)(_  )___/ ) _ (  )__)  )   /
 \___)(__)(__)(____)(___/(__)(__)(_)\_)   \___)(____)(__)  (_) (_)(____)(_)\_)
"""


def encrypt(original_text, shift_amount):
    result = ""
    for char in original_text:
        if char in alphabet:
            #posicao da letra 
            index  = alphabet.index(char)
            #shift e da a volta a lista
            new_index = (index + shift_amount) % len(alphabet)
            result += alphabet[new_index]
        else:
            result += char
    print(f"You have encrypted your message: {result}")

def decrypt(original_text, shift_amount):
    result = ""
    for char in original_text:
        if char in alphabet:
            #posicao da letra 
            index  = alphabet.index(char)
            #shift e da a volta a lista
            new_index = (index - shift_amount) % len(alphabet)
            result += alphabet[new_index]
        else:
            result += char
    print(f"You have decrypted your message: {result}")

def CaesarCipher():
    gameOver = True
    while gameOver:
        direction = input("Type 'encode' to encrypt or 'decode' to decrypt: \n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number: \n"))

        if(direction == "encode"):
            encrypt(text,shift)
        elif (direction == "decode"):
            decrypt(text,shift)
        else:
            print("You have to write 'encode' or 'decode' to use the program")
        stillPlaying = input("Type 'yes' if you want to go again. Otherwise type 'no'")
        if(stillPlaying == 'no'):
            print("👋 Exiting Caesar Cipher.")
            gameOver = False
print(banner)
CaesarCipher()
