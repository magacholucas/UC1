def montar_carrinho():
    carrinho=[]
    # criamos lista vazia
    print("=== BEM VINDO AO SUPERMERCADO PYTHON ==")
    # LAÇO DE REPETIÇÃO PARA CAPTURAR MULTIPLOS ITENS
    while True:
        produto=input(("Digite um produto (ou digite 'sair'):"))
        if produto.lower() == 'sair':
            break
        carrinho.append(produto)
        print(f"-> '{produto}' adicionado ao carrinho com sucesso!\n")
        # exibe o resultado final
        print("\n=== SEU CARRINHO DE COMPRAS ===")
        if len(carrinho) ==0:
            print ("Seu carrinho esta vazio.")
        else:
            # exibe os itens do carrinho
            for item in carrinho:
                print(f"- {item}")
    print (f"\ total de itens no carrinho: {len(carrinho)}")

# testando a funcao
montar_carrinho()
