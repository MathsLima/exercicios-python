"""Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares."""

lista = []

for i in range(10):
    numero = int(input("Digite o numero: "))
    lista.append(numero)

conta_pos = 0
conta_neg = 0

for num in lista:
    if num % 2 == 0:
        conta_pos = conta_pos + 1
    else:
        conta_neg = conta_neg + 1

print("Numeros inseridos: ", lista)
print("Quantidade de numeros positivos: ", conta_pos)
print("Quantidade de numeros negativos: " , conta_neg) 
    