'''Faça um programa que leia tres numeros e mostre qual é o maior e qual é o menor.'''

print("Digite # numeros que vou colocar em ordem pra vc!!!")

a= int(input("Digite o primeiro numero"))
b= int(input("Digite o segundo numero"))
c= int(input("Digite o terceiro numero"))

if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print ("menor {}".format (menor))
print ("maior {}".format(maior))


