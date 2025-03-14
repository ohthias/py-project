import random

ranNum = random.randint(1, 10)

print("Adivinhação")
inNum = int(input("Digite um número 1-10: "))

while inNum != ranNum:
    if inNum < ranNum:
        print("Ele é maior")
    else: 
        print("Ele é menor")
    inNum = int(input("Tente novamente: "))
print("Você acertou!")