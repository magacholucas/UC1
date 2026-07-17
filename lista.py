nomes = ["joão","ana","bruno"]
print (f"listagem de nomes {nomes}")
#para adicionar o nome na lista
nomes.append("Carlos")
print (f"listagem de nomes atualizada {nomes}")
n=input("Digite um nome a ser excluido => ")
# remove item
nomes.remove(n)
print (f"listagem de nomes atualizada {nomes}")
# ordena a lista
nomes.sort()
print (f"listagem de nomes atualizada {nomes}")
# len contas quantos itens tem na lista
l = len(nomes)
print(f"a lista tem {l} nomes")