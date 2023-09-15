# #Aula 29
# #importar biblioteca randint | ELA SERVE PARA GERAR NÚMEROS ALEATÓRIOS
from random import randint

print('Vamos jogar par ou impar?')
print('Escolha um número de 1 a 10')
print("---------------------------")
seuNumero = int(input('Insira seu número: '))

print('Agora, escolha (P) para par e (I) para impar')
suaEscolha = input('Insira sua escolha: ')

pcNumero = randint(1, 10)

soma = seuNumero + pcNumero
resultado = ""

if soma % 2 == 0:
    if suaEscolha.lower() == 'p':
        resultado = 'Deu PAR, você ganhou!'
    else:
        resultado = 'Deus PAR, você perdeu!'
else:
    if suaEscolha.lower() == 'i':
        resultado = 'Deu IMPAR, você ganhou!'
    else:
        resultado = 'Deu IMPAR, você perdeu!'

print('Você digitou', seuNumero, ' e escolheu', suaEscolha)
print('O computador digitou ', pcNumero)
print(resultado)