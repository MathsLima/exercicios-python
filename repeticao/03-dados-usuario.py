"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
"""
while True:
    nome = input("Digite o nome: ")
    if len(nome)  > 3:
        print("Nome ", nome)
        break
    else:
        print("Digite um nome com mais de 3 caracteres")


while True:
    idade = input("Digite sua idade: ")
    idade = int(idade)
    if idade > 0 and idade < 150:
        print("Idade ", idade)
        break
    else:
        print("Digite uma idade entre 0 e 150 anos")


while True:
    salario = input("Digite seu salario: ")
    salario = int(idade)
    if salario > 0:
        salario == salario
        print("Salario de ", salario)
        break
    else:
        print("Digite um salario maior que 0")


while True:
    sexo = input("Digite seu sexo: ")
    if sexo == "m" or sexo == "f":
        print("Sexo ", sexo)
        break
    else:
        print("Digite um sexo valido")
   

print("Dados:")
print("Nome: ", nome)
print("Idade: ", idade)
print("Salario: ", salario)
print("Salario: ", salario)

    