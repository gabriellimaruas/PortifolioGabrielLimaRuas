#Aula 33
#busca sequencial ou linear

#Tendo por base uma lista com os valores 10, 15, 33, 25, 37, 20. Crie um programa para
#encontrar um determinado valor nesta lista

lista = [10, 15, 33, 25, 37, 20]

numero = int(input('Digite o número que você que encontrar: '))

local = -1

for posicao in range(0, len(lista)):
    if lista[posicao] == numero:
        local = posicao
        break
if local > -1:
    print(numero, 'encontrado na posição', local)
else:
    print(numero, 'não encontrado!')