for alu in range(3):
    nome = input("Digite o nome do aluno ")
    n1= int(input ("informe nota 1 "))
    n2= int(input ("informe nota 2 "))
    n3= int(input ("informe nota 3 "))
    media = (n1+n2+n3)/3
    if media >= 7:
        print(f"{nome} a sua média é {media:.2f} voce esta aprovado")
    elif  media < 5:
        #case media>5 and media<6:
        #    print(f"{nome} a sua média é {media:.2f} voce esta em recuperação")
        print(f"{nome} a sua média é {media:.2f} voce esta reprovado")
    else :
        print(f"{nome} a sua média é {media:.2f} voce esta em recuperação")
