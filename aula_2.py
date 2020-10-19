# -+= coding: UTF-8 -+-
#   --------------------   AULA 2  --------------------   #


# exc 5
'''b
var1 = 10
var1 = 120

print(var1)
'''


# exc 6
'''
var_1 = 2
var_2 = 5.99
var_3 = "Python"


print(var_1 * var_2)
print(var_1 * var_3)
print(var_2 * var_1)
'''


# exc 7 
'''
nota1 = 10.0
nota2 = 6.0
nota3 = 8.0

media = (nota1 + nota2 + nota3) / 3
 
print("A sua média foi", media)
'''


#exc 8
'''
celsius = 25
Fahr = (celsius * 1.8) +32

print(Fahr, "ºF")
'''


#exc 9
'''
espaco = 600
tempo = 30

vm = espaco / tempo
print(vm)
'''
'''
#exc 10

valor_1 = "A"
valor_2 = "a"


print(valor_1 > valor_2)
print(valor_1 >= valor_2)

print(valor_1 < valor_2)
print(valor_1 <= valor_2)

print(valor_1 == valor_2)
print(valor_1 != valor_2)
'''


#exc 11

num_1 = 0
num_2 = 1

# VERDADEIRO --> var_1 < var_2
# FALSO --> var_1 > var_2


print("---------- OPERADOR LÓGICO E ------------")
print("V ^ V =", var_1 < var_2 and var_1 < var_2)
print("V ^ F =", var_1 < var_2 and var_1 > var_2)
print("F ^ V =", var_1 > var_2 and var_1 < var_2)
print("F ^ F =", var_1 > var_2 and var_1 > var_2)
print(" ")





print("---------- OPERADOR LÓGICO OU ------------")
print("V v V =", var_1 < var_2 or var_1 < var_2)
print("V v F =", var_1 < var_2 or var_1 > var_2)
print("F v V =", var_1 > var_2 or var_1 < var_2)
print("F v F =", var_1 > var_2 or var_1 > var_2)
print(" ")





print("---------- OPERADOR LÓGICO NOT ------------")
print("¬V =",  not(var_1 < var_2))
print("¬F =", not (var_1 > var_2))
print(" ")



print("---------- OPERADOR LÓGICO SE...ENTÃO ------------")
print("V --> V =", not(var_1 < var_2) or (var_1 < var_2))
print("V --> F =", not(var_1 < var_2) or (var_1 > var_2))
print("F --> V =", not(var_1 > var_2) or (var_1 < var_2))
print("F --> F =", not(var_1 > var_2) or (var_1 > var_2))
print(" ")



''' p   q     p ---> q

    V   V        V
    V   F        F
    F   V        V
    F   F        V

"Vera Felicia Falsa"

'''

