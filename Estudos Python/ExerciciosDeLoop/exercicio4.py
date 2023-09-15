#EXERCÍCIO 4
#Faça um programa que leia 5 números e informe o maior e o menor número.

lista = []
while len(lista) < 5:
    numeros = input('Insira um valor para adicionar a lista: ')
    lista.append(numeros)
maior = max(lista)
menor = min(lista)
print(lista)
print('O maior valor da lista é ', maior, 'e o menos valor da lista é', menor)