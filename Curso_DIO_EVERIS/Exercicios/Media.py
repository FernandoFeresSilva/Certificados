notaA= float (input("Informe a primeira nota: "))
notaB= float (input("Informe a segunda nota: "))

#calcular a media

mediafinal = (notaA + notaB) / 2

#verificação
if mediafinal >= 7.0:
    print ("A Media: %.1f - Aprovado " % mediafinal)
else:
    print ("A Media: %.1f - Reprovado " % mediafinal)