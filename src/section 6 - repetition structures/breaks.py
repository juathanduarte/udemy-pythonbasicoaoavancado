# Saindo de loops com break

# Exemplo 1

for numero in range(1, 10):
    if numero == 5:
        break
    print(numero)

# Exemplo 2

while True:
    resposta = input('Você gostaria de sair? [sim/não]')
    if resposta == 'sim':
        break