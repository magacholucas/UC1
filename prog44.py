nome = ""
while nome != "SAIR":
    nome= input ("Nome ou SAIR para parar : ").upper()
    if nome == "SAIR":
        break 
    print (f"O nome digitado é {nome}")
