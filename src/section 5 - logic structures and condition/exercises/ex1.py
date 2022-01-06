# Faça um programa que receba dois números e mostre qual deles é o maior.

numberOne = int(input("Digite o primeiro número: "))
numberTwo = int(input("Digite o segundo número: "))

if numberOne > numberTwo:
    print(f"O primeiro número ({numberOne}) é maior que o segundo ({numberTwo})")
else:
    print(f"O segundo número ({numberTwo}) é maior que o primeiro ({numberOne})")