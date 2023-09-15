#Aula 40
#Criando um jogo de Jackpot
#Você inicia com um crédito de R$ 10,00
#Você precisar puxar a manivela da máquina para girar 3 roletas internas
#Cada uma das roletas possui 6 frutas
#O resultado de cada uma das roletas é mostrado no painel da máquina, são três mostradores
#Se ao término do giro das roletas cada um dos mostradores do painel mostrar a mesma fruta você ganha mais R$ 10,00
# #No caso de os dois primeiros mostradores ou os dois últimos mostradores do painel mostrarem a mesma fruta você ganha R$ 2,00
#Caso cada um dos mostradores mostrem uma fruta diferente você perde R$ 1,00

import random

credito = 10
jogar = True
frutas = ['laranja', 'abacaxi', 'morango', 'uva', 'banana', 'melancia']

while jogar:
    m1 = random.choice(frutas)
    m2 = random.choice(frutas)
    m3 = random.choice(frutas)

    print('Créditos:', credito)
    print("---------------------")
    print(m1,m2,m3)
    print('---------------------')

    if m1 == m2 and m2 == m3:
        print('Uau! Você bateu o Jackpot e ganhou +R$10,00')
        credito += 10
    elif (m1 == m2 or m2 == m3) and m1 != m3:
        print("Parabens! Voce ganhou +R$2,00")
        credito += 2
    else:
        print("Sem sorte desta vez! Voce perdeu -R$1,00")
        credito -= 1
    if credito <= 0 or input("Deseja jogar mais uma rodada S/N?") not in "Ss":
        jogar = False

print("Fim de Jogo")
print("Total-->", credito)