# RECEBENDO DADOS DO USUÁRIO

#print("Qual seu nome? ")
#printnome = input()
nome = input("Qual seu nome? ")

#print("Seja bem-vindo(a) %s" % nome)
#print("Seja bem-vindo(a) {0}".format(nome))
print(f"Seja bem-vindo(a) {nome}")

#print("Qual sua idade? ")
#idade = input()
idade = int(input("Qual sua idade? "))

#print("O(a) %s tem %s anos" % (nome, idade))
print(f"O(a) {nome} tem {idade} anos")

print(f"O(a) {nome} nasceu em {2021 - idade}.")