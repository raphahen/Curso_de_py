import random
import datetime

random = random.randint(1,10)
numero = int(input("Digite um número: "))

if numero == random:
        print("Você ganhou")
else:
        print("Você perdeu")



data = datetime.datetime.now()
print(data)
