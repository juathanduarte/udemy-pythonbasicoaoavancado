# TIPO FLOAT

# Errado

valor = 1,44
print(valor)
print(type(valor))

# Certo

valor = 1.44
print(valor)
print(type(valor))

# É possível fazer dupla atribuição

valor1, valor2 = 1, 44
print(valor1)
print(valor2)
print(type(valor1))
print(type(valor2))

#Podemos converter float para int

res = float(valor)
print(res)
print(type(res))