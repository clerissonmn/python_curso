# -*- coding: utf-8 -*-
"""
Curso de Introdução à programação com python
Parte 1: Conceitos iniciais
"""
#%%###################
## Comandos básicos ##
######################
print(123)
#%%#################
## Tipos de dados ##
####################

## int (inteiro)
print(type(123))

## float
print(type(123.))

print(type(23/2))

## booleano (True or False)
print(type(True))

## strings 
print('String')
print(type('isso é um texto'))
print(type("isso é um texto"))
print(type("""
           isso é um texto de várias
           linha
           ok??
           """))
print("'O Cara' é o apelido de ")

# Print misturando texto e número

print('O valor de x é: ',123,'e y: ',321)


#%%#########################
## Operadores matemáticos ##
############################
# Aritméticos
# + soma
# - subtração
# / divisão
# * multiplicação
# ** potência
#
print('Operadores lógicos')
print('-----------------')
# Lógicos 
# >
print('10 > 0: ', 10 > 0 )

# <
print('10 > 0: ', 10 < 0 )

# >=
print('10 >= 10: ', 10 >= 10 )

# <=
print('10 <= 10: ', 10 <= 10 )
print('9 <= 10: ', 9 <= 10 )

# and
print('False and False: ', False and False)
print('False and True: ', False and True)
print('True and False: ', True and False)
print('True and True: ', True and True)

# or
print('')
print('False or False: ', False or False)
print('False or True: ', False or True)
print('True or False: ', True or False)
print('True or True: ', True or True)

# not
print('')
print('not True', not True)


#%%############
## Variáveis ##
###############
print('Variáveis')
print('-----------------')
A = 100
B = 30
soma = A + B
print('a soma A + B é', soma)

print('')
C = True
D = False
resultado = C and D
print('C and D: ', resultado)

#%%######################
## Comandos de Decisão ##
#########################
print('')
M = 6
print(M >= 6)
## if else
if M >= 6:
    print('Passou !!!!! É 50% !!!!!!!')
else:
    print('Ops, ainda é 40% :-[ ')


#%%###############
## Exercício!!! ##
##################
# 1)a) Criar três variáveis AV1, AV2 e atribuir a elas uma nota de um aluno
#   b) Calcular a média desse aluno para dudas
#   c) Decidir se o aluno vai fazer ou não a AV3

AV1 = 10
AV2 = 10
media_provas = (AV1 + AV2)/2
print('media = ',media_provas)

if (media_provas >= 6):
    print('Não fará AV3')
else:
    print('Sim, fará AV3')
    print('Ok??')

#%%########################
## Comandos de repetição ##
###########################
## for
print('laço for')
print('========')
i = 0 
print(i)

i = i+1
print(i)

i = i+1
print(i)

print('Usando uma forma mais eficiente')

for i in range(0, 11):
    print('A idade do aluno', i, 'é :',1.5*i)

########## 
print('\n======\n')

import math

A = 9

print( math.sqrt(A) )    
math.sinh(2)
math.cos(math.pi /3 )

import numpy as np

######### 

x = np.linspace(0,2*math.pi)
y = np.sin(x)

import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))
plt.plot(x,y)

import seaborn as sns
sns.barplot(x=x,y=y)
    
    

