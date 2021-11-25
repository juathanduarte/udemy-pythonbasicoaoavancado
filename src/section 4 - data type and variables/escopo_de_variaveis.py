numero = 42 # Variável global
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))

numero = 42

if numero > 10:
    novo = numero + 10 # Variável local
    print(novo)

print(novo)