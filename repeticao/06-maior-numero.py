"""Faça um programa que leia 5 números e informe o maior número."""

lista = []

for i in range(5):
    num = int(input("Digite um numero: "))
    lista.append(num)

maior = max(lista)
menor = min(lista)

print("Numeros: ", lista)
print("Maior numero: ", maior)
print("Menor numero: ", menor)
