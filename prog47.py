y=1
ac=0
while y!= 0:
    y=int(input("Digite o codigo do produto "))
    if y == 1:
        ac=ac+4
        print ("Arroz R$ 4,00")
    elif  y == 2:
        ac=ac+7
        print ("Feijao R$ 7,00")
    elif  y == 3:
        ac=ac+5
        print ("Macarrão R$ 5,00")
    else :
        print(f"{y} Produto não encontrado")

print(f"O total da sua compra é R$ {ac:.2f} ")