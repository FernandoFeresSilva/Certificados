qtd =0
soma =0
media=0
valor = float (input("Digite um Numero de 0 até 10: "))

while (valor > 2):
    soma = soma + valor
    qtd = qtd + 1
    valor = float(input("Digite um numero de 0 até 10: "))

media = soma /qtd
print ("\n Total da Soma: ", soma)
print ("\n Quantidade de valores digitados: ", qtd)
print("\n Media dos valores: ", media)
