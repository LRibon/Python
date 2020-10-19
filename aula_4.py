# -+= coding: UTF-8 -+-
#   --------------------   AULA 4  --------------------   #


'''
# 1)

-------------------- INDENTAÇÃO --------------------


É o recuo do texto em rel. a margem, utilizando o espaçamento em 4. 
Os blocos são delimitados pela profundidade da identação, isto é, os códigos rente a margem 
são do 1° nivel hierarquico e os que estão a 4 espaços são de 2° nivel, 8 espaços são de 3° e
etc.


Todos os blocos são delimitados pela profundidade da indentação e por isso, a sua importância,
 é vital para um programa em Python.
Todos os blocos são delimitados pela profundidade da indentação e por isso, a sua importância
, é vital para um programa em Python!

Existem 2 tipos de blocos: os de Código e os de Comentários

-------------------- BLOCO DE CÓDIGO --------------------

É um conjunto de instrução que estão na msm margem a esquerda



print(nivel 1)#primeiro nível hierárquico

if(True):
    print(nível 2)#segundo nível hierárquico


Este é um bloco de comentários e essa é a primeira linha
agora, estamos na segunda linha de comentário(s)

A recomendação é que utilizemos, ou 1 tabulação, ou então, 4 espaços.


'''

'''

# 2)

nota_1 = 9.5
nota_2 = 7.0
nota_3 = 6.0

media = (nota_1 + nota_2 + nota_3)/3

if (media >= 6):
	print("Você foi APROVADO com média", round(media, 1))
 

# exc pra IF e ELSE

Pai_On = 1
Pai_Off = 2

if (Pai_On > Pai_Off):
	print("O Pai ta ON")

else:
	print("O Pai ta Off")

'''
'''

# 3) 

nota_1 = 4.5
nota_2 = 7.3
nota_3 = 9.0
media = (nota_1 + nota_2 + nota_3)/3

if (media >= 6.0):
	print("Você foi APROVADO com média", round(media, 1))

else:
	print("Você foi REPROVADO com média", round(media, 1))


'''
# ELIF
'''
a = 4
b = 5
 
if (a > b):
	print("A é maior que B, com valor de A:", a)
elif (b > a):
	print("B é maior que A, com valor de B:", b)
else: 
	print("A e B são iguais, com valor de A e B:", a, "e", b)
'''
'''
# 4)

nota_1 = 2.0
nota_2 = 3.0
nota_3 = 6.0
media = (nota_1 + nota_2 + nota_3)/3

if (media >= 6):
	print("Você foi APROVADO com média", round(media, 1))
elif (media >= 4.0) and (media < 6.0):
	print("Você está de EXAME com média", round(media, 1))
else: 
	print("Você foi REPROVADO, com média:", round(media, 1))


'''
# 5)

'''

a = 2
b = 1

if (a > b):
	if a > 0:
		print("Variavel A maior e positiva", a)
	else:
		print("Variavel A maior e negativa", a)

elif (b > a):
	if b >= 0:
			print("Variavel B maior e positiva", b)
	else:
		print("Variavel B maior e negativa", b)

else:
	print("Os valores de A e B são iguais:", a, "e", b)

"""
ex
"""
'''
#variaveis
'''
np1 = float(input('Informe sua primeira nota:'))
np2 = float(input('Informe sua segunda nota:'))
np3 = float(input('Informe sua terceira nota:'))
media = round((np1+np2+np3)/3,2)
'''
#programa 
'''

if (media >= 6):
	print ('Voce foi aprovado',media)

elif (media >= 4.9 and media <= 5.9):
	print ('Voce esta de exame',media)
else:
	print ('Voce foi reprovado',media)
'''
#ex1
'''
'''
#variaveis
'''
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc =  round(peso/(altura**2),1)

'''
#condicoes
'''
if (imc < 18.5):
	print ('Voce esta muito abaixo do peso ideal:',imc)

elif (imc >= 18.5 and imc <=24.9):
	print ('Voce esta no peso ideal:',imc)

if (imc >= 25.0 and imc <= 29.9):
	print ('Voce esta um pouco acima do peso ideal:',imc)

elif (imc >= 30.0 and imc <= 34.9):
	print ('Obesidade classe I:',imc)

if (imc >= 35.0 and imc <= 39.9):
	print ('Obesidade classe II:', imc)

if (imc > 40.0):
	print ('Obesidade classe III:', imc)

'''
#ex 2
'''
'''
#variaveis
'''
salario = 1045.00
renda = int(input("Digite a sua:"))
classe_social = round(quantidade_salarios/salario,2) 
'''
#condicoes

'''
if (classe_social > 15):
	print ('Sua classe social e A, voce recebe a quantidade de salarios de:', classe_social)

elif (classe_social > 5 and  classe_social <= 15):
	print ('Sua classe social e B, voce recebe a quantidade de salarios de:',  classe_social)

if ( classe_social > 3 and  classe_social <= 5):
	print('Sua classe social e C, voce recebe a quantidade de salarios de:', classe_social)

if ( classe_social > 1 and  classe_social <= 3):
	print ('Sua classe social e D,voce recebe a quantidade de salarios de:', classe_social)

if  ( classe_social == 1):
	print ('Sua classe social e E,voce recebe a quantidade de salarios de:', classe_social)

'''
#ex3
'''
'''
#variaveis
'''
salario = float(input('Digite seu salario:'))
aumento1 = salario*20/100+salario
aumento2 = salario*15/100+salario
aumento3 = salario*8/100+salario
'''
#condicoes
'''
if (salario <= 1200):
	print ('O aumento sera de 20%, seu novo salario e:',aumento1)
elif (salario > 1200 and salario <= 2000):
	print('O seu aumento sera de 15%, seu novo salario e:',aumento2)
if (salario > 2000):
	print ('O seu aumento sera de 8%, seu novo salario e:',aumento3)

'''
#exc4
'''
ladoA = int(input('Digite o lado A:'))
ladoB = int(input('Digite o lado B:'))
ladoC = int(input('Digite o lado C:'))

if (ladoA == ladoB): 	
	if(ladoB == ladoC):
		print ('Equilatero')
	else:
		print ('Isoceles')
elif (ladoA == ladoC):
	print ('isoceles')
elif (ladoB == ladoC):
	print ('Isoceles')
else:
	print ('escaleno')

'''
#5)

'''

ano = 2050

c = ano//100
n = ano-19*(ano//19)
k = (c-17)//25
i = c-c//4 - (c-k)//3 + 19*n + 15
i = i-30*(i//30)
i = i - (i//28)*(1-(1//28))*(29//(i+1))*((21-n)//11)
j = ano + ano//4 + i +2 -c +c//4
j = j - 7*(j//7)
l = i - j
mes = 3 + (l+40)//44
dia = l + 28 - 31*(mes//4)


print("A páscoa do ano", ano, "será no mês", int(mes), "e no dia", int(dia))
print(c)

'''


#1) Desenvolva um programa para calcular o índice de Massa Corpórea. O usuário deve digitar a altura e o peso,
# e o programa deve retornar o valor do IMC e a sua respectiva condição, conforme a tabela a seguir.

'''
peso = 120
altura = 1.60
IMC = (peso / (altura**2))

if (IMC < 18.5) :
    print('Abaixo do peso normal')
    
elif 18.5 <= IMC <= 24.9 :
    print('Peso normal')
    
elif 25.0 <= IMC <= 29.9 :
    print('Excesso de peso')
    
elif 30.0 <= IMC <= 34.9 :
    print('Obesidade classe I')
    
elif 35.0 <= IMC <= 39.9 :
    print('Obesidade classe II')
    
else :
    print('Obesidade classe III')
'''







#2) Uma empresa deseja efetuar uma pesquisa de campo para saber a Lista de Classes Sociais...

'''
salario = 20000
salario_min_valor = 998.00
salario_min_qntd = salario / salario_min_valor

if salario_min_qntd <= 1 :
    print('Classe Social E')
elif 1 < salario_min_qntd <= 3 :
    print('Classe Social D')
elif 3 < salario_min_qntd <= 5 :
    print('Classe Social C')
elif 5 < salario_min_qntd <= 15 :
    print('Classe Social B')
else :
    print('Classe Social A')
'''





#3) Uma empresa deseja conceder um aumento escalonadoaos seus funcionários conforme os rendimentos apontados a seguir...

'''
salario = 2005

if salario <= 1200.00 :
    escalonado =(salario*0.20)
    print('Seu novo salario é: ',salario + escalonado)
elif 1200.00 < salario <= 2000.00 :
    escalonado =(salario*0.15)
    print('Seu novo salario é: ',salario + escalonado)
else :
    escalonado =(salario*0.08)
    print('Seu novo salario é: ',salario + escalonado)
'''





#4) Faça um programa que dado os valores dos catetos e hipotenusa, informe qual a sua classificação. Conforme figuras a seguir.

'''
AB = 30
AC = 10
BC = 10

if AB == AC == BC :
    print('Seu triangulo é Equilatero')
elif AB == AC  :
    print('Seu triangulo é Isosceles')
elif AB != AC != BC :
    print('Seu triangulo é Escaleno')
else :
    print('O valor inserido não corresponde a nenhum triangulo')
'''




#5) Para calcular a data da Páscoa para qualquer ano no calendário Gregoriano (o calendário civil no Brasil), usa-se a seguinte fórmula,
# com todas as variáveis e operações inteiras, com os restos das divisões ignorados. Usase a para ano, m para mês, e d para dia.

'''
a = 2021

c = a//100
n = a - 19*(a//19)
k = (c-17)//25
i = c - c//4 - (c-k)//3 + 19*n + 15
i = i - 30*(i//30)
i = i - (i//28)*(1-(1//28)*(29//(i+1))*((21-n)//11))
j = a + a//4 + i + 2 - c + c//4
j = j -7*(j//7)
l = i - j
m = 3 +(l+40)//44
d = l + 28 - 31*(m//4)

print('A páscoa será dia',int(d),'no mês', int(m),'e no ano', int(a))
'''