#Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro.

number = int(input("Digite um número: "))
tripleNumber = number * 3 + 1
doubleNumber = number * 2 - 1

print(f"A soma é {tripleNumber + doubleNumber}")