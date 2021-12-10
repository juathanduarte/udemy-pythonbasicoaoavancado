# Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo em vista que o desconto foi de 12%

valor = float(input("Digite um valor: "))

discount = valor * 0.12

print(f"O valor com 12% de desconto é {valor - discount}")