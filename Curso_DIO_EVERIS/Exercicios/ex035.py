"Faça um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou não formar um triangulo"
print("-="*20)
print("Analisador de Triangulo")
print("-="*20)
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

if a < b + c and b < a + c and c < a + b:
    print("Estas retas podem ser um triangilo reta 1= {:.0f}, reta 2= {:.0f}, reta 3= {:.0f}".format(a,b,c))
else:
    print("estes valores não formam um triangulo")