x=int(input("Digite o valor "))
tab=0
for i in range(0,11):
    # range(5) é a mesma coisa que o de cima vai de 0 a 5 
    tab=i*x
    #tab+= x  é a mesma coisa que acima codigo do python
    print (f"{x} x {i} = {tab} ")