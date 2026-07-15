y=1
ac=0
item=1
while y!= 0:
    y=int(input("Digite o valor do item "))
    print(f"Item {item} R$  {y:.2f} ")
    item+=1
    ac+=y
gorjeta=ac*0.1
valordaconta = ac*1.1
print(f"O total da sua conta é R$ {ac:.2f} ")
print(f"O total da gorjeta é R$ {gorjeta:.2f} ")
print(f"O total a pagar é R$ {valordaconta:.2f} ")