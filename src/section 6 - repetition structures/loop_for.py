# # # Loop for
# # # Estrutura de repetição

# # # for item in interavel:
# # #       EXECUTA O LOOP

# # nome = 'Geek University'
# # lista = [1, 3, 5, 7, 9]
# # numeros = range(1, 10)

# # # Exemplo 1

# # for letra in nome:
# #     print(letra)

# # # Exemplo 2

# # for numero in lista:
# #     print(numero)

# # # Exemplo 3

# # for numero in range(1, 10):
# #     print(numero)

# # # Exemplo 4

# # for i, letra in enumerate(nome):
# #     print(nome[i])

# # # Exemplo 5

# # for i, letra in enumerate(nome):
# #     print(letra)

# # # Exemplo 6

# # for _, letra in enumerate(nome):
# #     print(letra)

# # # Exemplo 7

# # for valor in enumerate(nome):
# #     print(valor)

# qtd = int(input('Quantas vezes esse loop deve rodar?'))
# soma = 0

# for n in range(1, qtd + 1):
#     num = int(input(f'Informe o {n}/{qtd} valor:'))
#     soma += num
# print(f'A soma dos valores foi {soma}')

nome = 'Geek University'

for letra in nome:
    print(letra, end='')