"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual
ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
"""

while True:
    usuario = input("Digite o seu nome de usuario: ")
    senha = input("Digite a sua senha: ")

    if usuario == senha:
        print("Usuario e senha não podem ser iguais, digite novamente")
    else:
        print("Usuario e senha cadastradas com sucesso!")