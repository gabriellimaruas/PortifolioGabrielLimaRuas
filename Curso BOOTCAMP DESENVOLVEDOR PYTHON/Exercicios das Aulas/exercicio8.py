#AULA 31
#Criando um jogo de adivinhação
#importa o random | ELE SERVE PARA GERAR NÚMEROS ALEATÓRIOS POR MEIO DO ALGORÍTIMO MESENNE TWIESTER.

import random
#para gerar números aleatórios no tipo float
print( random.random() )
#para gerar números entre sua escolha
print( random.randint(1,5) )
#para sortear valores de uma lista
print( random.choice(["amarelo","verde","azul","branco"]) )


#Gere um número entra 1 e 5 que será armazenador em uma variável
#O programa deverá pedir para o usuário adivinhar qual o número que o computador tem em "mente".
#O número informado pelo usuário poderá então ser armazenado em uma variável. Neste jogo o usuário
#terá 3 chances de adivinhar qual o número, caso adivinhe o número ele ganha,
# caso contrário o computador vence.

import random

aleatorio = random.randint(1,5)

rodada = 1
print('O computador escolheu um número entre 1 e 5. Adivinhe em apenas 3 tentativas.')

while rodada <= 3:
    print('Esta é a tentativa', rodada)
    nEscolhido = int(input('Insira o número: '))

    if nEscolhido == aleatorio:
        print('Parabéns, você acertou!')
        break
    else:
        print('Incorreto, tente novamente!')


    rodada += 1
    print('-----------------------------------------------')

if rodada > 3:
    print('O número que o computador pensou foi', aleatorio)
    print('Desculpe, o computador venceu o jogo!')