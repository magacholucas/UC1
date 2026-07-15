anasc = int(input ("Digite o ano do seu nascimento "))
idade = 2026 - anasc
if idade >= 18 and idade <= 65:
    print (f"sua idade é {idade} Maior de idade") 
elif idade >= 65:
    print ("Idoso")
else: 
    print ("Menor de idade ")
