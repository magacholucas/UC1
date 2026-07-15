def ida(nasci):
    idade = 2026 - nasci
    if idade >= 18 and idade <= 65:
        print (f"sua idade é {idade} Maior de idade") 
    elif idade >= 65:
        print ("Idoso")
    else: 
        print ("Menor de idade ")

   
nasci = int(input("Digite o ano do seu nascimento "))
ida(nasci)
