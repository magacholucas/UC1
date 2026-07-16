''' 
calculo de media informando 4 notas
'''
def nota(n1,n2,n3,n4):

    media = (n1+n2+n3+n4)/4
    print(f"Sua Média é  {media:.2f}")
    if media >= 7: 
        print ("Aprovado") 
        print ("Parabéns")
    elif media >=5:
        print ("Recuperação") 
    else: 
        print ("Reprovado")
        print ("Estude Mais")

n1 = float(input ("Informe nota1 "))
n2 = float(input ("Informe nota2 "))
n3 = float(input ("Informe nota3 "))
n4 = float(input ("Informe nota4 "))

nota(n1,n2,n3,n4)


