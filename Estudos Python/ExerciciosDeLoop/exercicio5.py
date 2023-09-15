#EXERCÍCIO 5
#Faça um programa que leia 5 números e informe a soma e a média dos números.

lista = []

while len(lista) < 5:
    numeros = int(input('Insira um valor para adicionar a lista: '))
    lista.append(numeros)
soma = 0
for total in lista:
    soma += total

media = soma/len(lista)
print('A soma dos números da lista é ',soma ,' e a média é de ', media)