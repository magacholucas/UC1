print ("PARQUE TECH PARK - CONTROLE DE ACESSO A MONTANHA RUSSA")
print (" ")
print (" ")
anasc = int(input ("Digite o ano do seu nascimento "))
idade = 2026 - anasc
''' bloco de comentario
teste de comentario
'''
ingresso = input ("O cliente possui ingresso (S) ou (N) ").upper()
if ingresso=="S" and idade >=12: 
    print ("Acesso liberado, divirta-se no brinquedo") 
elif  ingresso=="S" and idade < 12:
    print ("Voce tem o ingresso, mais não tem a idade minima de 12anos") 
else :
    print ("Acesso negado voce precisa de um ingresso")
print (" ")
print (" ")