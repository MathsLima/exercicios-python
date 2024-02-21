"""
Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue pedindo 
até que o usuário informe um valor válido.
"""
while True:
    numero = input("Digite um numero: ")
    numero = int(numero)

    if numero <= 10 and numero >= 0:
        print("Numero valido! " + f'{numero}')
        break
    else: 
        print("Digite um numero valido: ")


    
