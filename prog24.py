n1 = int(input("Digite numero 1 "))
n2 = int(input("Digite numero 2 "))
print ("1 - Somar")
print ("2 - Subtrair")
print ("3 - Multiplicar")
print ("4 - Dividir")
opcao = int(input("Escolha a Operação "))
match opcao:
    case 1:
        ''' 
        trbalhar sempre com variavel
        operacao=n1+n2
        '''
        print ("A Soma é ", n1+n2)
    case 2:
        print ("A Subtração é ", n1-n2)
    case 3:
        print ("A multiplicação é ", n1*n2)
    case 4:
        print ("A divisão é ", n1/n2)
    case _:
        print ("Opção invalida")
        print ("teste de commit")
 print ("teste de push pelo teste  vccod 3")