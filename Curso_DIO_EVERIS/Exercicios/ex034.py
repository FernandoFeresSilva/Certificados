"Faça um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento. .\
    Para salarios superiores a R$ 1.250,00, calcule um almento de 10% .\
    Para salarios inferiores ou iguais, o aumento é de 15 % "

salario = float(input("Digite seu Salario: "))

if salario > 1250.00:
    salario = (salario * 10 / 100) + salario
    print ("salario recebeu um aumento de 10% = {:.2f}".format(salario))
else:
    salario = (salario * 15/100) + salario
    print("seu novo Salario com aumento de 15% é de {:.2f}".format(salario))

print("Seja Feliz")
