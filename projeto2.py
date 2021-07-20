'''
Escreva um programa que. ao inciar gera um valor aleatorio de 1 a 10 e permite que o usuario
chute um numero até o valor aleatório geraddo no inicio do programa seja chutado corretamente

O programa deve informar  se o chute foi acima, abaixo ou igual ao valor aleatorio gerado no
inicio do programa.

# Método 5Q's para montar um algoritmo:
Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e peça mais
informações/investigue mais até você compreender completamente o problema.)

1. Quais são os dados da entrada necessários?
- valor aleatorio de 1 a 10
- chute do usuario

2. O que devo fazer com estes dados?
Eu devo comprar o chute do usuario com o valor aleatorio que foi gerado no inicio do programa e
dizer se o chute foir maior, menor ou igual ao valor que foi gerado no inicio do programa

3. Quais são as restrições deste problema?
- um valor aleatorio de 1 a 10

4. Qual é o resultado esperado?
- O resultaddo esperado é que o programa deve informar  se o chute foi acima, abaixo ou igual ao valor aleatorio gerado no
inicio do programa.

5. Qual é sequência de passos a ser feitas para chegar ao resultado esperado?
input valor_aleatorio de 1 a 10
input chute
if chute > valor_aleatorio
    print "Chute foi maior que o valor gerado"
if chute < valor_aleatorio
    print "Chute foi menor que o valor gerado"
if chute = valor_aleatorio
    print "Você acertou!"        
'''

import random

valor_aleatorio = random.randint(1,10)
acertou = False
while acertou == False:
    chute = int(input('Chute um valor de 1 a 10: '))
    if chute > valor_aleatorio:
        print ('Chute foi maior que o valor gerado')
    elif chute < valor_aleatorio:
        print ('Chute foi menor que o valor gerado')
    elif chute == valor_aleatorio:
        acertou = True
        print('Você acertou!')    
