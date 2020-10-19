'''
nome = input('Qual seu nome? ')
idade = input('Qual sua idade? ')
peso = input('Qual seu peso? ')
print("Seu nome é:",nome, "Sua idade é:",idade, "Seu peso é:",peso)
'''

#Desafio 01 
#Crie um script que leia o nome do usuario e mostre uma mensagem de boas-vindasde acordo com o valor digitado

'''
nome = input('Qual seu nome? ')
print("Boas vindas",nome,"!","Bem vindo!")
'''

#Desafio 02
#Crie um script que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada

'''
dia = input("Insira seu dia de nascimento: ")
mes = input("Insira seu mês de nascimento: ")
ano = input("Insira seu ano de nascimento: ")

print('Você nasceu em: ',dia,'de',mes,'de',ano,'.','Correto?')
'''

#Desafio 03
#Crie um script que leia dois números e tente mostrar a soma entre eles

num_1 = int(input('Insira o primeiro número: '))
num_2 = int(input('Insira o segundo número: '))
s = num_1 + num_2
print('A soma entre {} e {} vale: {}!'.format(num_1, num_2, s))