'''
Projeto - Medidor de Velocidade

Levandoo em consideração a velocidade máxima permitidda de 80km em uma determinadad rua. Crie um
programa que recebe do usuario um valor que representa a velocidade e com base nessa velocidade diga se ele tomou uma multa leve,
grave ou gravissima. Levando em consdireção que se a pessoa estiver abaixo da velocidade máxima seu programa deve exibir "Não houve multa", caso esteja até
10km acima, deve exibir: "levou multa leve", caso esteja entre 11 a 20km acima da velociddade máxima, exibir:
"levou multa grave", e caso esteja acima de 20km da velocidadde máxima, exiba: "levou multa gravissima"

# Método 5Q's para montar um algoritmo:
Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e peça mais
informações/investigue mais até você compreender completamente o problema.)

1. Quais são os dados da entrada necessários?
-velocidade do usuario

2. O que devo fazer com estes dados?
-Levando em consdireção que se a pessoa estiver abaixo da velocidade máxima seu programa deve exibir "Não houve multa", caso esteja até
10km acima, deve exibir: "levou multa leve", caso esteja entre 11 a 20km acima da velociddade máxima, exibir:
"levou multa grave", e caso esteja acima de 20km da velocidadde máxima, exiba: "levou multa gravissima"

3. Quais são as restrições deste problema?

4. Qual é o resultado esperado?
Levando em consdireção que se a pessoa estiver abaixo da velocidade máxima seu programa deve exibir "Não houve multa", caso esteja até
10km acima, deve exibir: "levou multa leve", caso esteja entre 11 a 20km acima da velociddade máxima, exibir:
"levou multa grave", e caso esteja acima de 20km da velocidadde máxima, exiba: "levou multa gravissima"

5. Qual é sequência de passos a ser feitas para chegar ao resultado esperado?
input velocidade
velocidade_maxima = 80
if velocidade < = velocidade_maxima
    print('Não levou multa')
if velocidade > velocidade_maxima e velocidade <= velocidade_maxima + 10
    print('Você levou multa leve')
if velocidade > velocidade_maxima ++11 e velocidade <= velocidade_maxima + 20
    print('Levou multa grave')
if velocidade > velocidade_maxima + 20:
    print('LEvou multa gravissima')
'''

velocidade = int(input('Digite sua velocidade: '))
velocidade_maxima = 80
if velocidade <= velocidade_maxima:
    print('Não levou multa')
elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima + 10:
    print('Levou multa leve')
elif velocidade >= velocidade_maxima + 11 and velocidade <= velocidade_maxima + 20:
    print('Levou multa grave') 
elif velocidade > velocidade_maxima + 20:
    print('Levou multa gravissima')           

