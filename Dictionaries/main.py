from os import system

#Codigo vai estar em um while
#pegar nome da pessoa
#Quanto e que a pessoa esta a apostar
#Perguntar se tem mais pessoas
    #Sim repete o processo e limpa a tela
#Nao mostra o valor mais alto

hammer = """
          __________
                  /
           )_______(
          |""""""""|_.-._,.---------.,_.-._
          |        | | |               | | ''-.
          |        |_| |_             _| |_..-'
          |________|  ''''-----------''  |_|
          )""""""""(
         /___________\\
       .-------------.
      /_______________\\
"""

print(hammer)
print("Welcome to the secret auction program")
record = {}
while(1):
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    newPerson = input("Are there any other bidders? Type 'yes' or 'no' \n")
    record[name] = bid
    if(newPerson == "no"):
        break
    system("clear")

for key in record:
    big = max(record)
print(f"The winner is {big} with a bid of ${record[big]}")