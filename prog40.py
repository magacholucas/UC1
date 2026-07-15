pessoas = {}
#cria tabela em branco tem que ser em {}
for i in range (2):
    nome= input ("Nome: ")
    idade= int(input("Idade: "))
    pessoas [nome] = idade
print (f"Dicionario completo: {pessoas}")