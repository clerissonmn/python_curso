# https://github.com/clerissonmn/python_curso

#%%###################
## Comandos básicos ##
######################
# Imprime na tela
print(123,321)
print(123 + 1)

# Retorna o tipo da variável
type(123)

#%%#################
## Tipos de dados ##
####################
print('Tipos de variáveis')
print('==================')

## int (inteiro)
print(type(10))

## float (real)
print(type(10.0))

## booleano (True or False)
print(type(False))

## strings 
print(type('walmir'))
print(type("Antonia Juliana"))

# Print misturando texto e número
print('')
print('O resultado da conta é',123,'ou','123.0anyfvj')


#%%############
## Variáveis ##
###############
nome = 'Daniela'
notaAV1 = 10
print('A nota de', nome, 'é', notaAV1)

#%%##########
## Slicing ##
#############

matricula = '400000682'
print(matricula[6:9])

matricula = '400000682'
nova_matricula = matricula[0] + matricula[6:9]
print(nova_matricula)

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
# Lógicos 
# >
# <
# >=
# <=
# and
# or
# not




#%%######################
## Comandos de Decisão ##
#########################
#if
print('\nComandos de Decisão')
print('-=-=-=-=-=-=-=-=-=-')



A = 1
B = 7
soma = A + B
print(soma)

print(soma < 5)

if soma < 5:
    print('Ok!')
else:
    print('Ops...')



#%%###############
## Exercício!!! ##
##################
# 1)a) Criar duas variáveis AV1, AV2 e atribuir uma nota de um aluno
#   b) Calcular a média desse aluno para dudas
#   c) Decidir se o aluno vai fazer ou não a AV3
AV1 = 5
AV2 = 5
media = (AV1 + AV2)/2

print(media)

if media < 6:
    print('Faz AV3')
else:
    print('Não Faz AV3')    
#%%
#2) a) Criar uma variável e inserir um número do tipo float
#   b) Decidam a qual faixa de valores ele pertence:
#   c) A:[0,10]
#      B:]10,20]
#      C:maior que 20

#a)   
A = float(input('Por favor, digite o valor de A: '))

#b)
if 0 <= A <= 10:
    print('A')
elif 10 < A <= 20:
    print('B')
elif A > 20:
    print('C')
else:
    print('nenhuma faixa')
    
#%%########################
## Comandos de repetição ##
###########################
## for
print('\nComandos de Repetição')
print('-=-=-=-=-=-=-=-=-=-=-=-')
i = 0
print(i)
i = i+1
print(i)
i = i+1
print(i)
i = i+1
print(i)
i = i+1
print(i)
i = i+1
print(i)

print('Forma mais inteligente')

for i in range(0,60001):
    #print(i)
    #print('Aluno',i,'está reprovado',)
    #print(i*2+1)
    
    if i > 1000: 
        break
    
    print('Já cansei!!!!!',i)
    

    
#%%######################
## Importaçao de dados ##
#########################
