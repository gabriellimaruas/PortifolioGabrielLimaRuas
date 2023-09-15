#SECAO 10
#SEGUNDO ROBO
#Pegar os dados de um pdf já criado e colocar essas dados em um arquvio excel

import time
import os
from openpyxl import Workbook
import PyPDF2

print('Iniciando robô...')
time.sleep(1)

# Abrir o arquivo PDF
filePdf = open('gastos.pdf', 'rb')

# Ler o arquivo PDF com o PdfFileReader()
lerPdf = PyPDF2.PdfReader(filePdf)

# Pegar o número de páginas com o len(lerPdf.pages)
numPag = len(lerPdf.pages)

# Escolher a página desejada
pagEscolhida = lerPdf.pages[0]

print('Lendo os dados do PDF...')
time.sleep(1)

# Extrair o conteúdo da página em formato de texto
extPdf = pagEscolhida.extract_text()

# Dividir o conteúdo em linhas usando '\n' como delimitador
parsed = extPdf.split('\n')

# Remover linhas vazias da lista
parsed = [linha.strip() for linha in parsed if linha.strip()]

# Criar uma lista para armazenar os elementos tratados
lista = []

# Adicionar os cabeçalhos à lista
lista.append(['Tipo', 'Valor', 'Forma de Pagamento'])

# Criar loop para adicionar os dados à lista
for i in range(1, len(parsed) - 2):
    linha = parsed[i].split()
    if len(linha) >= 3:
        lista.append(linha[:3])

print(lista)


print('Criando Arquivo Excel')

#criar arquivo excel
wb = Workbook()
ws = wb.active

#looping para add os dados pro excel com a planilha selecionada
for row in lista:
    ws.append(row)

#salvar
wb.save('gastospdf.xlsx')

os.startfile('gastospdf.xlsx')

# print(lista)



