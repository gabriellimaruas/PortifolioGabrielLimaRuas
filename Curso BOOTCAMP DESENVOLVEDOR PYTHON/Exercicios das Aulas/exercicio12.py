#Seção 5
#Aula 37
#função para retornar o maior valor de uma lista

def maior(plista):
    mValor = 0
    for posicao in plista:
        if posicao > mValor:
            mValor = posicao
            print(mValor)
    return mValor
lista = [1, 10, 3, 2, 5, 4, 7, 6, 9, 8]
m = maior(lista)
print(m)