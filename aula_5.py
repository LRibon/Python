# -------------------------------------------- aula 5 --------------------------------------------
'''
x = 1

while (x <= 10):
	print(x)
	x += 1
	
'''
'''

x = 1              #condição inicial

while (x <= 10):   #condiçãofinal
	
	x += 1         #incremento

------------------------------------------------

WHILE

	INCREMENTO
		1° Forma
			x += 1
		2° Forma
			x = x + 1


	DECREMENTO
		1° Forma
			x -= 1
		2° Forma
			x = x - 1
	
''' 


'''

tabuada = 5
x = 1

while (x <= 10):
	print(tabuada, "x", x, "=", tabuada * x)
	x += 1

'''


# ---------------- EXERCICIOS ----------------


#1)

'''

x = 1
nome ="Ribon"
while (x <= 100):
	print(x, "-", nome)
	x += 1

'''

#2)

'''

fatorial = 5
x = 1
result = 1

while (x <= fatorial):
	result = result * x
	x += 1

print(result)

'''

#3)

'''

x = 500
resto = 0

while (x >= 1):
	if (x % 2 == resto):
		print(x)
	x -= 1


'''


#4)

'''

x = 1
resto = 1

while (x <= 500):
	if (x % 2 == resto):
		print(x)
	x += 1

'''


#5)

'''

from random import randint

x = 1

while (x <= 6):
	numero = randint(1,60)
	print(numero)
	x += 1

'''





