nome = input("Digite seu nome ")
print (nome)
cargo = input (" por favor informe seu cargo ").upper()
if cargo=="CAIXA": 
    salario=1500
elif  cargo=="GERENTE":
    salario=4000 
elif  cargo=="VENDEDOR":
    salario=4000 
else :
    salario =0
inss =  salario* 0.12
if salario > 2000.00:
    irrf = salario * 0.14
else :
    irrf = salario * 0.8
print(f"Salario bruto  {salario:.2f} Salario Liquido R$ {salario-irrf-inss:.2f}")