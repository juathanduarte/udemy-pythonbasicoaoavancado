# Leia um número real. Se o número for positivo imprima a raiz quadrada. Do contrário,  imprima o número ao quadrado. Se

import math

number = int(input("Digite um número: "))

if number > 0:
    print(f"A raiz quadrada de {number} é {math.sqrt(number)}")
else:
    print(f"O número {number} ao quadrado é {number * number}")