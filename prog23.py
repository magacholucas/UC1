codigo = int(input("Digite o codigo de erro "))
match codigo:
    case 200:
        print ("Sucesso ! Tudo certo com a sua requisição")
    case 400:
        print ("Erro do cliente: Requisição malformada")
    case 404:
        print ("Erro pagina não encontrada")
    case 500|503:
        print ("Erro no servidor. Nosso sistema esta invalido no momento")
    case _:
        print ("Codigo de Erro não reconhecido")