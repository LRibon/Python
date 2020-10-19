# -+= coding: UTF-8 -+-
#   --------------------   AULA 3  --------------------   #



# 1) Faça um progama para o calculo de baskara

'''

a = 1
b = 2
c = -3


delta = (b**2) - (4*a*c)

x_1 = (- b + (delta**0.5))/2*a 
x_2 = (- b - (delta**0.5))/2*a 

print("X' =", x_1)
print("X' =", x_2)

'''


# 2) Calcule o salario do mano brown

'''

bruto = 998
inss = bruto * 0.08
conv = 22.45
liquido = bruto - (inss + conv)

print("O seu salário =", liquido)

'''
'''
tente usar input nesses exc

"round" vai aredondar o valor dentro do ()
round(NomeDaVarável, NúmeroDeCasasDecimal)
'''
'''

print("O seu salário =", liquido, 2)
print(liquido, 2)




# 5) Calcule o salario do cara 

fixo = 998
venda = 48995
comissao = venda * 0.05
bruto = fixo + comissao

inss = bruto * 0.08
conv = 22.45
desc = inss + conv

liquido = bruto - desc

print("O seu salário =", liquido)



# 4) Equivalencia de Morgan

var_1 = 0
var_2 = 1


# VERDADEIRO --> var_1 < var_2
# FALSO --> var_1 > var_2


print("---------- MORGAN (LADO ESQUERDO ------------")
print("~ (V ^ V) =", not (var_1 < var_2 and var_1 < var_2))
print("~ (V ^ F) =", not (var_1 < var_2 and var_1 > var_2))
print("~ (F ^ V) =", not (var_1 > var_2 and var_1 < var_2))
print("~ (F ^ F) =", not (var_1 > var_2 and var_1 > var_2))
print(" ")



print("---------- MORGAN (LADO DIREITO ------------")
print("~V v ~V) =", (not var_1 < var_2) or (not var_1 < var_2))
print("~V v ~F) =", (not var_1 < var_2) or (not var_1 > var_2))
print("~F v ~V) =", (not var_1 > var_2) or (not var_1 < var_2))
print("~F v ~F) =", (not var_1 > var_2) or (not var_1 > var_2))
print(" ") 


# 5) Bicondicional

var_1 = 0
var_2 = 1


# VERDADEIRO --> var_1 < var_2
# FALSO --> var_1 > var_2


print("---------- OPERADOR LÓGICO SE E SOMENTE SE ------------")
print("V <--> V =", (not (var_1 < var_2) or (var_1 < var_2)) and (not (var_1 < var_2) or (var_1 < var_2)))
print("V <--> F =", (not (var_1 < var_2) or (var_1 > var_2)) and (not (var_1 > var_2) or (var_1 < var_2)))
print("F <--> V =", (not (var_1 > var_2) or (var_1 < var_2)) and (not (var_1 < var_2) or (var_1 > var_2)))
print("F <--> F =", (not (var_1 > var_2) or (var_1 > var_2)) and (not (var_1 > var_2) or (var_1 > var_2)))
print(" ")