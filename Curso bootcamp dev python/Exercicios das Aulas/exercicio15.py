#Aula 41
#Removendo duplicidade
#Escreva um programa que chame uma função passando como parametro uma lista com valores duplicados,
#a função deve retornar uma nova lista que contém todos os elementos da primeira lista menos os valores
#duplicados.

def dup(pLista):
    novaLista = []
    for p in pLista:
        if p not in novaLista:
            novaLista.append(p)
    return novaLista

def dup2(pLista):
    return list(set(pLista))

lista = [1,2,3,4,3,2,1]
print(dup(lista))
print(dup2(lista))