print("-=" * 50)
print(
    "Faça a leitura de vendas dos 4 primeiros meses e calcule se o vendedor recebera 10 ou 3 % de abono \nSe meta de 5000,00 for atiginda abona de 10% caso contrario abono de 3% ")
print("-=" * 50)

m1 = float(input("Informe o valor de vendas de Janeiro: "))
m2 = float(input("Informe o valor de vendas de Fevereiro: "))
m3 = float(input("Informe o valor de vendas de Março: "))
m4 = float(input("Informe o valor de vendas de Abril: "))
total = float (m1 + m2 + m3 + m4)
media = (m1 + m2 + m3 + m4) / 4

if media >= 5000:
    abono = media * 10 / 100
    print("Total de vendas dos 4 meses " , total)
    print("Parabens sua media foi de {:.0f} vc atigiu a meta de 5000 recebera 10% de abono, \nsegue valor a receber {}".format(
            media, abono))
else:
    abono = media * 3 / 100
    print("Total de vendas dos 4 meses ",total)
    print("Vc precisa se esforçar mais não conseguiu atingir a meta da media de 5000, sua media foi de {:.0f} \nseu abono será de {}".format(
            media, abono))

print("BOAS VENDAS")
