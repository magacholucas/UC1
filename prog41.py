carros = {}
#cria tabela em branco tem que ser em {}
for i in range (2):
    carro= input ("Carro ")
    marca= input ("Marca ")
    valor= float(input("valor: "))
    carros [carro] = {
        "marca":marca,
        "valor":valor
    }
    carros [carro] = valor
print (f"Lista de Carros: {carros}")