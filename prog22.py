dia = input("Digite o dia da Semana ")
match dia:
    case "Segunda" | "Terça" | "Quarta" | "Quinta" | "Sexta":
        print ("Dia da semana. Dia de programar")
    case "Sabado" | "Domingo":
        print ("fim de semana. Hora de descansar")
    case _:
        print ("Dia invalido")