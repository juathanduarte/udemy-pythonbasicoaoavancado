# Faça um programa que receba a altura e o sexo de uma pessoa e calcule seu peso ideal, utilizando as seguintes fórmulas (onde h corresponde a altura)
# Homens: (72.7 * h) - 58
# Mulheres: (62.1 * h) - 44,7

personHeight = float(input("Digite sua altura: "))
personSex = input("Qual seu sexo (M ou F): ")

if personSex == 'M':
    print(f"Seu peso ideal é {(72.7 * personHeight) - 58}")
if personSex == 'F':
    print(f"Seu peso ideal é {(62.1 * personHeight) - 44}")