tempe= int(input ("Informe a temperatura "))
if tempe < 18:
    print (f"A temperatura informada é {tempe} ** Esta frio **") 
elif tempe >= 18 and tempe <= 30:
    print (f"A temperatura informada é {tempe} ** Agradavel **") 
else: 
    print (f"A temperatura informada é {tempe} ** Calor **")