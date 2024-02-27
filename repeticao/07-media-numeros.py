"""Faça um programa que leia 5 números e informe a soma e a média dos números."""

lista =[]

for i in range(5):
    num = int(input('Digite um numero: '))
    lista.append(num) 

soma = sum(lista)
media = soma / 5

print("Soma: ", soma)
print("Media: ", media)

    