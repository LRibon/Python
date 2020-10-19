# Aula 01 - Exercícios 1 a 5

'''
1) Oque é certificação em tecnologia da informação?

R: É um documento que comprova a proficiência do profissional, em alguma determinada tecnologia ou produto da área de TI.





2) Em Python existe 4 níveis de certificações. Quais são esses níveis?

R: - Beginning Python --> conhecimento básico na linguagem.

   - Getting More Out of Python --> criação de interface gráfica, desenvolvimento de banco de dados e envio de e-mail por python.
   
   - The Python Environment --> criação de API's, manipulação de dados textuais e outras técnicas.
   
   - Advanced Python --> desenvolver soluções complexas na ferramenta. 
   
   
   
   
   
   
3) Qual o caminho no Brasil para se tirar uma ceritifcação Python?

R: Ir a uma instituição de ensino respeitável, pois na internet pode-se ocorrer golpes ou  o certificado não possui um valor impactante. O aconselhado
é ter projeto e códigos abertos dispónivel (GitHub) para a empresa analisar e ver se você realmente sabe progamar.





4) Quanto a salários e carreira, como Python está posicionado no mercado de trabalho?

R: Python está crescendo no rank de popularidade e atualmente (2020) já ultrapassou Java e esta em primeiro lugar como lingaugem mais usada.
A seguir algumas areas que utilizam Python em seus códigos e há demanda de trabalho:
- Industria de Jogos
- Desenvolvimento Web e Frameworks
- Big Data
- Inteligência Artificial
- Ciência de Dados

Em questão de salário o desenvolvedor Python ganha equivalente a R$ 6.452 no Brasil





5) Qual a média salarial de um desenvolvedor Python?

R: Como dito na questão anterior a média no Brasil é de R$ 6.452, porém existe detalhes que lhe dão um bônus:

- Conhecimento Framework Javascript
    R$ 6.742
- Desenvolvedor Júnior
    R$ 5.003
- Desenvolvedor Pleno
    Entre R$ 5.502 e R$ 6.818
- Desenvolvedor Sênior 
    R$ 9.196
'''


# Fim Exercicios Aula 01














# Aula 02 - Exercícios 5 a 10


#5) Desenvolva um programa que uma mesma variável é declarada duas vezes, com valores diferentes
'''
var_1 = 5
var_1 = 10
print(var_1)
'''


'''
A segunda var_1 foi impressa
'''





#6) Desenvolva um programa com três variáveis, com os seguintes valores:

''''
var_1 = 2
var_2 = 5.99
var_3 = 'Python'
'''

#Realize as operações pedidas

# Operações de soma

'''
print(var_1 + var_2)
'''

'''
print(var_1 + var_3)
'''

'''
print(var_2 + var_3)
'''

# Operações de multiplicação

'''
print(var_1 * var_2)
'''

'''
print(var_1 * var_3)
'''

'''
print(var_2 * var_3)
'''


'''
Apenas o "print(var_1 + var_2)" e "print(var_1 * var_2)" foram executados, pois ambos possuem valores númericos enquanto o "var_3" é uma string 
e não pe possível realizar operçãoes matematicas entre uma string e um valor numerico.
'''






#7) Faça um programa que receba 3 notas e retorne a média.

'''
nota_1 = 6
nota_2 = 8
nota_3 = 7

print((nota_1 + nota_2 + nota_3) / 3)
'''

'''
O valor da média foi igual a 7
'''






#8) Faça um programa que efetue a conversão de Celsius para Fahrenheit.

'''
Celsius = 25
Fahrenheit = Celsius * 1.8 + 32
print('A temperatura Celsius em Fahrenheit é de: ', Fahrenheit)
'''

'''
A temperatura Celsius em Fahrenheit é de 77,0
'''






#9) Faça um programa que calcule a velocidade média.

'''
distancia = 10
tempo =2
VM = distancia / tempo
print(VM)
'''

'''
A velocidade media foi de 5.0
'''






#10) Faça um programa calcular a área do circulo.

'''
Pi = 3.14
raio = 10
S = Pi * (raio ** 2)
print(S)
'''

'''
O valor da área do circulo é aprox de 314
'''


# Fim Exercicios Aula 02














# Aula 03 - Lista 1 a 5

#1) Faça um programa para o calculo de baskara.

'''
a = 1
b = 2
c = -3
delta = (b**2) - (4*a*c)


x_1 = (-b + delta**0.5)/(2*a)

x_2 = (-b - delta**0.5)/(2*a)
print(x_1, x_2)
'''






#2) Faça um programa que receba o valor do salário bruto
#(R$ 998,00) de um trabalhador e efetue os descontos de:
#INSS de 8% e convênio médico R$ 22,45. No final dos
#cálculos, informe qual o salário liquido do usuário.

'''
salario = 998.00
inss = 0.08
convmdc = 22.45
desconto_inss = salario*inss
print(desconto_inss)
salario_final = salario - desconto_inss - convmdc
print(salario_final)
'''






#3) Faça um programa que calcule o salário de um vendedor de veículos...  Ao final o programa deve retornar o valor do salário liquido
#do trabalhador.

'''
salario_fixo = 998.00

venda = 48995
comissao = venda * 0.05

salario_bruto = salario_fixo + comissao

inss = salario_bruto * 0.08
convmdc = 22.45
desc = inss + convmdc

salario_liquido = salario_bruto - desc

print(salario_liquido)
'''






#4) Desenvolva um programa que prove a lei de equivalência notável De Morgam.


# ---------------------------------------- Morgan Lado Esquerdo ---------------------------------------- #

p = 0
q = 1

# VERDADEIRO --> var_1 < var_2
# FALSO --> var_1 > var_2

'''
print(('~ (V ^ V) ='), not (p < q and p < q))
print(('~ (V ^ F) ='), not (p < q and p > q))
print(('~ (F ^ V) ='), not (p > q and p < q))
print(('~ (F ^ F) ='), not (p > q and p > q))
print('')
'''    
# ---------------------------------------- Morgan Lado Direito ---------------------------------------- #
'''
print(('~ (V ^ V) ='), (not p < q) or (not p < q))
print(('~ (V ^ F) ='), (not p < q) or (not p > q))
print(('~ (F ^ V) ='), (not p > q) or (not p < q))
print(('~ (F ^ F) ='), (not p > q) or (not p > q))
print('')
'''

'''
A lei de equivalência é verdadeira
'''






#5) Desenvolva um programa que a bicondicional pela lei de equivalência notável.

# ---------------------------------------- Morgan Bicondicional ---------------------------------------- #
'''
print(('V <--> V ='), (p < q) == (p < q))
print(('V <--> F ='), (p < q) == (p > q))
print(('F <--> V ='), (p > q) == (p < q))
print(('F <--> F ='), (p > q) == (p > q))
'''
# ---------------------------------------- Morgan Bicondicional ---------------------------------------- #
'''
print(('V --> V ='), (p < q) and (p < q))
print(('V --> F ='), (p < q) and (p > q))
print(('F --> V ='), (p > q) and (p < q))
print(('F --> F ='), (p > q) and (p > q))
'''
# ---------------------------------------- Morgan Se Então ---------------------------------------- #
'''
print(('V --> V ='), (p < q) <= (p < q))
print(('V --> F ='), (p < q) <= (p > q))
print(('F --> V ='), (p > q) <= (p < q))
print(('F --> F ='), (p > q) <= (p > q))
'''

# Fim Lista Aula 03














# Aula 04 - Exercícios 1 a 5


#1) Desenvolva uma pesquisa acerca de regras de indentação em Python?
'''
R:Indentar é o recuo do texto em relação a sua margem, ou seja, se antes de escrevermos uma instrução, utilizando 4 espaçamentos 
da margem esquerda até a instrução propriamente dita, podemos dizer que a indentação utilizada possui 4 espaços.
Em Python, a indentação possui função bastante especial, até porque, os blocos de instrução são delimitados pela profundidade da 
indentação, isto é, os códigos que estiverem rente a margem esquerda, farão parte do primeiro nível hierárquico. Já, os códigos 
que estiverem a 4 espaços da margem esquerda, estarão no segundo nível hierárquico e aqueles que estiverem a 8 espaços, estarão no 
terceiro nível e assim por diante.
'''






#2)Faça um programa que seja inserida 3 notas e calcule a media.
    # Se a média for maior ou igual a 6,0, retorne a frase: “Você foi aprovado com media (valor da média)”

'''
N1 = 7.0
N2 = 4.0
N3 = 10.0
media = (N1 + N2 + N3) / 3

if media >= 6.0 :
    print('Você foi aprovado com a media: ',media,'!')
'''






#3) Faça um programa que receba 3 notas, calcule a média.
# Se a média for maior ou igual a 6,0, retorne a frase: “Você foi aprovado com média (valor)”.
# Se a media for menor do que 6,0, retorne a fase: “Você foi reprovado com média (valor)”.

'''
N1 = 6.0
N2 = 4.0
N3 = 5.0
media = (N1 + N2 + N3) / 3

if media >= 6.0 :
    print('Você foi aprovado com a media: ',media,':)')
else :
    print('Você foi reprovado: ',media,':(')
'''







#4) 4) Faça um programa que receba 3 notas, calcule a media.
# Se a média for maior ou igual a 6,0, retorne a frase: “Voce foi aprovado com media (valor)”.
# Se a média for estiver entre 4,0 e 5,9, retorne a frase: “Voce esta de exame sua nota foi (valor)”.
# Se a media for menor do que 4,0, retorne a fase: “Voce foi reprovado com media (valor)

'''
N1 = 2.0
N2 = 4.0
N3 = 5.0
media = (N1 + N2 + N3) / 3

if media >= 6.0 :
    print('Você foi aprovado com a media: ',media,':)')
elif media >= 4.0 and media <= 5.9 :
    print('Você esta de exame, sua nota foi de: ',media,':/')
else :
    print('Você foi reprovado: ',media,':(')
'''






#5) Escreva por extenso o programa a seguir:

'''
a = 2
b = 2

if a > b:
    if a >= 0:
        print('Variavel "a" maior e positiva:',a)
    else : 
        print('Variavel "a" maior e negativa:',a)    

elif b > a:
    if b >= 0:
        print('Variavel "b" maior e positiva:', b)
    else :
        print('Variavel "b" maior e positiva:', b)

else :
        print('Os valores de "a" e "b" são iguais','a: ', a,'e','b: ', b)
'''

# Fim Exercicios Aula 04















# Aula 05 - Exercicios Extras


#1) Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o
# usuário informe um valor válido. (!!!VALIDAÇÕES DE VALORES!!!)

'''
nota = float(input('Insira uma nota entre 0 e 10:' ))

while (nota < 0) or (nota > 10)  :
    nota = float(input('Não pode ser menor que 0 ou maior que 10! Tente novamente!'))
print('Sua nota é de: ',nota)
'''




#2) Faça um programa que gere 5 números aleatórios e informe o maior número.

'''
x = 0
while x <= 5 :
    from random import randint
    numeros = [(randint(0,15))]
    print(numeros)
    x += 1
    
maior = max(numeros)
print('Os numeros gerados foram: ',numeros)
print('O maior numero gerado foi: ',maior)
'''


    
# Fim Exercicios Extras Aulas 05















# Aula 06 - Desafio!


#5) Faça um programa, sorteie um número entre 1 e 6. Após isso, o usuário escolha um valor entre 1 e 6

'''
import random
sorteio = random.randint (1,6);

while True :
    num_inserido = int(input('Insira um numero entre 1 e 6: '))
    print(num_inserido)
    if num_inserido == sorteio :
        print('Voce acertou maldito!') 
        break
'''

# Fim Desafio Aula 06  
















#Lista Condicional

#1) As Organizações Tabajara resolveram dar um aumento de salário aos... Após o aumento ser realizado, informe na tela:

# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

'''
salario_user = float(input('Insira seu salário: '))
aumento_20p = salario_user * 0.20
aumento_15p = salario_user * 0.15
aumento_10p = salario_user * 0.10
aumento_5p = salario_user * 0.05
salario_novo = 0

if (salario_user <= 280) and (salario_user > 0) :
    salario_novo = salario_user + aumento_20p
    print('Seu salario inicial era de: ', salario_user,'! Seu aumento foi de 20 porcento com valor de:', aumento_20p,'! E seu salario final é de: ', salario_novo,'!!!')
    
    
elif (salario_user > 280) and (salario_user < 700)  :
    salario_novo = salario_user + aumento_15p
    print('Seu salario inicial era de: ', salario_user,'! Seu aumento foi de 15 porcento com valor de:', aumento_15p,'! E seu salario final é de: ', salario_novo,'!!!') 
    
elif (salario_user > 700) and (salario_user < 1500) :
    salario_novo = salario_user + aumento_10p
    print('Seu salario inicial era de: ', salario_user,'! Seu aumento foi de 10 porcento com valor de:', aumento_10p,'! E seu salario final é de: ', salario_novo,'!!!') 
    
else  :
    salario_novo = salario_user + aumento_5p
    print('Seu salario inicial era de: ', salario_user,'! Seu aumento foi de 5 porcento com valor de:', aumento_5p,'! E seu salario final é de: ', salario_novo,'!!!')  
''' 





#2) Crie um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: 

'''
while True :
    sexo = input('Insira seu sexo: ')
    if (sexo == 'F') or (sexo == 'M') :
        print('Ok!')
        break
    else: 
        print('Sexo Inválido!')
'''




#3) Faça um programa que determine e retorne se um número é par ou ímpar. 

'''
num = int(input('Insira um número maior que 0: '))

while num > 0 :
    if (num % 2) == 0 :
        print('O numero é par!')
        break
    if (num % 2) == 1 :
        print('O numero é ímpar!')
        break 
'''





#4) Faça um programa que receba a idade por meio de uma variável e imprima a sua condição (obrigatória, optativa ou proibida), em relação 
# ao ato de votar, conforme apresentado abaixo:

'''
idade = int(input('Insira sua idade: '))
            
while idade > 0 :
    if idade < 16 :
        print('Proibido')
        break
    elif (16 <= idade < 18) or (idade >= 65) :
        print('Optativo')
        break
    else :
        print('Obrigatório')
        break
'''





#5) Faça um programa que gere um número aleatório de 0 a 50, e retorne:

'''
import random
num_sorteio = random.randint(0, 50)

if 0 <= num_sorteio <= 10 :
    print(num_sorteio, '--> Primeira fase de teste.')
elif 11 <= num_sorteio <= 20 :
    print(num_sorteio, '--> Segunda fase de teste.')
elif 21 <= num_sorteio <= 30 :
    print(num_sorteio, '--> Terceira fase do teste.')
elif 31 <= num_sorteio <= 40 :
    print(num_sorteio, '--> Quarta fase do teste.')
else :
    print(num_sorteio, '--> Quinta fase de teste.')
'''





#6) Escreva um algoritmo que leia um número e informe se ele é divisível por 10, por 5 ou por 2 ou se não é divisível por nenhum deles

'''
num = int(input('Insira um numero: '))

while num > 0 :
    if (num % 10) == 0 and (num % 5) == 0 and (num % 2) == 0 :
        print('Esse numero é divisível por 10, 5 e 2')
        break
    
    elif (num % 10) == 0 and (num % 2) == 0 :
        print('Esse numero é divisível por 10 e 2')
        break
    
    elif (num % 5) == 0 :
        print('Esse numero é divisível apenas por 5')
        break
    
    elif (num % 2) == 0 :
        print('Esse numero é divisível apenas por 2')
        break
    else :
        print('Esse numero não é divisível pro 10, 5 e 2')
        break
'''





#7) Criar um algoritmo que informe a quantidade total de calorias de uma refeição a partir do usuário que deverá informar o prato, a sobremesa e a bebida.

'''
print('Pratos:')
print('1 - Vegetariano')
print('2 - Peixe')
print('3 - Frango')
print('4 - Carne')

p = float(input('Insira qual o seu prato: '))

if (p >= 1) and (p <= 4) :
    if p == 1 :
        pcal = 180
    elif p == 2 :
        pcal = 230
    elif p == 3 :
        pcal = 250
    elif p == 4 :
        pcal = 350
else :
    print('Não há este item no cardápio.')
    
        
print('Sobremesa:')
print('1 - Abacaxi')
print('2 - Sorvete diet')
print('3 - Mouse diet')
print('4 - Mouse de chocolate')

s = int(input('Insira qual o sua sobremesa: '))   

if (s >= 1) and (s <= 4) :
    if s == 1 :
        scal = 75
    elif s == 2 :
        scal = 110
    elif s == 3 :
        scal = 170
    elif s == 4 :
        scal = 200
else :
    print('Não há este item no cardápio.')
     
        
print('Bebidas:')
print('1 - Chá')
print('2 - Suco de Laranja')
print('3 - Suco de Melão')
print('4 - Refrigerante')

b = int(input('Insira qual o sua bebida: '))


if (b >= 1) and (b <= 4) :
    if b == 1 :
        bcal = 20
    elif b == 2 :
        bcal = 70
    elif b == 3 :
        bcal = 100
    elif b == 4 :
        bcal = 65
else :
    print('Não há este item no cardápio.')
    
    
      
if (p >= 1) and (p <= 4) and (s >= 1) and (s <= 4) and (b >= 1) and (b <= 4) :
    print('O número total de calorias é de: ', pcal + scal + bcal)
 '''  
 
 
 
 
#8) Qualquer número natural de quatro algarismos pode ser dividido...

'''
soma = 0
num = int(9801)

while num > 0 :
    soma += num % 100
    num = int(num /100)
print(soma)]

raiz = float(num) ** 0.5

if soma == raiz :
    print('Vc acetou parabens!')
'''
 
 
# Fim Lista Condicional














# Revisão de conteúdo - 1° Bimestre






# Fim Revisão de conteúdo - 1° Bimestre















