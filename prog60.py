cursos = ["Python","HTML"]
print (f"listagem de nomes {cursos}")
n=input("Digite um Curso a ser incluido => ")
cursos.append(n)
print (f"listagem de cursos atualizada {cursos}")
n=input("Digite um Curso a ser excluido => ")
cursos.remove(n)
print ("listagem de cursos atualizada")
for x in cursos:
    print(x)