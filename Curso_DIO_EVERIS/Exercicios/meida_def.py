def lernotas():
    n=float(input('Digite um nota para o aluno(a):'))
    return n


def resultado(n1,n2):
    media=(n1+n2)/2
    print ("nota 1: ",n1)
    print ("nota 2: ",n2)
    print ("Media: ",media, "Resultado: ", end="")
    if media >=7:
        print ("Aprovado")
    else:
        print("Reprovado")


a = lernotas()
b = lernotas()
resultado(a,b)
