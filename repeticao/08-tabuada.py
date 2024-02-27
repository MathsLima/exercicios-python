"""Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro. 
O usuário deve informar de qual numero ele deseja ver a tabuada"""

num = int(input("Digite o numero que deseja: "))

for i in range(11):
    valor = num * i
    print( num, "X" , i, "=", valor)