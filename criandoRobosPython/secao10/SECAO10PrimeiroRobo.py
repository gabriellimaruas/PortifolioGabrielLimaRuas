#SECAO 10
#PRIMEIRO ROBO
#Pegar os dados de um arquivo de texto já criado e colocar essas dados em um arquvio excel

from openpyxl import Workbook

print('Iniciando robo...')
print('Lendo dados do arquivo de texto...')

#abrir o arquivo de texto | 1 argumento é o nome do arquivo,
# 2 argumento é a forma com que vamos abrir ele,
# 3 argumento definir a linguagem (acentos)
arquivoTXT = open('gastos.txt', 'r', encoding='utf-8')

#ler o arquivo
arquivo = arquivoTXT.read()

#colocar o arquivo no formato de lista
lista = arquivo.splitlines()

#separa os elementos por virgulas com split
for i in range(0,len(lista)):
    lista[i] = lista[i].split(',')

print('Criando arquivo excel...')

#Criar arquivo excel
wb = Workbook()
#selecionar a planilha ativa
ws = wb.active

#adicionar dados da lista para o arquivo excel
for row in lista:
    ws.append(row)

wb.save('gastos.xlsx')





