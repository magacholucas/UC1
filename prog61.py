def lista_de_compras():
    lista=[]
    while True:
        produto=input(("Digite um produto (ou digite 'sair'):"))
        if produto.lower() == 'sair':
            break
        # verificar se o item ja existe
        if produto in lista:
            print ("item ja cadastrado")
        else:
            lista.append(produto)
            print(f"-> '{produto}' adicionado ao carrinho com sucesso!\n")
        # exibe o resultado final
            print("\n=== SEU CARRINHO DE COMPRAS ===")
            if len(lista) ==0:
                print ("Seu carrinho esta vazio.")
            else:
                # exibe os itens do carrinho
                for item in lista:
                    print(f"- {item}")
    print (f"\ total de itens na lista: {len(lista)}")

# testando a funcao
lista_de_compras()