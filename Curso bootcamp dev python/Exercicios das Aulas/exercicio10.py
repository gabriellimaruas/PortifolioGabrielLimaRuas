#Aula 34
#Algorítmo de ordenação Bubble Sort

#ORGANIZANDO UMA LISTA

lista = [5, 4, 3, 2, 1]
contador = True

while contador:
    contador = False
    for posicao in range(4):
        a = lista[posicao]
        b = lista[posicao+1]
        if b < a:
            lista[posicao] = b
            lista[posicao+1] = a
            contador = True
            print(lista)

print(lista)