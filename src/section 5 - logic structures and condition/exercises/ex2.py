# Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.

import math

number = int(input("Digite um número: "))

if number > 0:
    print(f"A raiz quadrada de {number} é {math.sqrt(number)}")
else:
    print("Número inválido!")