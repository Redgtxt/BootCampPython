import random

PEDRA = r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
PAPEL = r"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
TESOURA = r"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

options = [PEDRA, PAPEL, TESOURA]
names = ["Pedra", "Papel", "Tesoura"]

while True:
    try:
        player_index = int(input("Escolhe 0=Pedra, 1=Papel, 2=Tesoura: ").strip())
        if player_index in (0, 1, 2):
            break
        print("Digite 0, 1 ou 2.")
    except ValueError:
        print("Digite um número válido.")

computer_index = random.randint(0, 2)

print(f"\nTu: {names[player_index]}\n{options[player_index]}")
print(f"PC: {names[computer_index]}\n{options[computer_index]}")

result = (player_index - computer_index) % 3
if result == 0:
    print("Empate")
elif result == 1:
    print("Ganhaste")
else:
    print("Perdeste")