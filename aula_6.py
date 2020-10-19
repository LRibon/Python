#   -------------------- Aula 6 --------------------   #

'''

numero = int(input("Entre com um valor: "))
result = 5 * numero
print(result)

'''

# float são para numeros REAIS (coloque antes do input)
# int são para numeros INTEIROS (coloque antes do input)


# 1)

'''

numero = int(input("Entre com um valor: "))
x = 1
while (x <= 10):
	print("A tabuada deste número é de:", numero, "X", x, "= ", numero * x)
	x += 1

'''

# 2)

'''

nome = input("Insira seu nome:" )
qtd = int(input("Insira quantas vezes seu nome sera impresso: "))

while (qtd >= 1):
	print(nome)
	qtd -= 1

'''

# 3)

'''

fatorial = int(input("Insira um valor desejado:" ))
x = 1
result = 1

while (x <= fatorial):
	result = result * x
	x += 1
print(result)

'''

# 4)

valor = int(input("Insira um valor: "))

if (valor >= 0) and (valor <= 33):
	result = valor ** 3
	print(result)
elif (valor >= 34) and (valor <= 66):
	result = valor ** 2
	print(result)
elif (valor >= 67) and (valor <= 100):
	result = valor - 10
	print(result)
else:
	print("Valor errado!")

print(result)