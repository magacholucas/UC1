nome = input ("Digite seu nome ")
n1 = float(input ("Informe nota1 "))
n2 = float(input ("Informe nota2 "))
n3 = float(input ("Informe nota3 "))
n4 = float(input ("Informe nota4 "))
media = (n1+n2+n3+n4)/4
print(f"{nome} Sua Média é  {media:.2f}")
if media >= 6: 
    print ("Aprovado") 
    print ("Parabéns")
else: 
    print ("Reprovado")
    print ("Estude Mais")