from selenium import webdriver as bot
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pyautogui as tempo
import pyautogui as posicaoMouse

#imports excel
from openpyxl import Workbook
#import para a fonte em negrito
from openpyxl.styles import Font

#Criar arquivo excel
workbook = Workbook()

#Criar planilha para armazenas os dados
planilha_dados = workbook.active
planilha_dados.title = 'DADOS'

#Definir o titulo de cada coluna
planilha_dados['A1'] = 'Estado'
planilha_dados['B1'] = 'Gentílico'
planilha_dados['C1'] = 'Capital'
planilha_dados['D1'] = 'Governador'
planilha_dados['E1'] = 'Pop. Estimada'
planilha_dados['F1'] = 'IDH'

#Aumentar a largura das colunas
colunaA = 'A'
nova_largura = 20
planilha_dados.column_dimensions[colunaA].width = nova_largura
colunaB = 'B'
nova_largura = 20
planilha_dados.column_dimensions[colunaB].width = nova_largura
colunaC = 'C'
nova_largura = 20
planilha_dados.column_dimensions[colunaC].width = nova_largura
colunaD = 'D'
nova_largura = 40
planilha_dados.column_dimensions[colunaD].width = nova_largura
colunaE = 'E'
nova_largura = 20
planilha_dados.column_dimensions[colunaE].width = nova_largura
colunaF = 'F'
nova_largura = 20
planilha_dados.column_dimensions[colunaF].width = nova_largura

#Colocar o titulo em negrito e aumentar o tamanho
celulaA = planilha_dados['A1']
celulaA.font = Font(bold=True)
celulaA.font = Font(size=16)
celulaB = planilha_dados['B1']
celulaB.font = Font(bold=True)
celulaB.font = Font(size=14)
celulaC = planilha_dados['C1']
celulaC.font = Font(bold=True)
celulaC.font = Font(size=14)
celulaD = planilha_dados['D1']
celulaD.font = Font(bold=True)
celulaD.font = Font(size=14)
celulaE = planilha_dados['E1']
celulaE.font = Font(bold=True)
celulaE.font = Font(size=14)
celulaF = planilha_dados['F1']
celulaF.font = Font(bold=True)
celulaF.font = Font(size=14)

navegador = bot.Chrome()
navegador.get('https://cidades.ibge.gov.br/')

lista = ['Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 'Espírito Santo', 'Goiás', 'Maranhão',
         'Mato Grosso', 'Mato Grosso Do Sul', 'Minas Gerais', 'Pará', 'Paraíba', 'Paraná', 'Pernambuco', 'Piauí',
         'Rio de Janeiro', 'Rio Grande Do Norte', 'Rio Grande Do Sul', 'Rondônia', 'Roraima', 'Santa Catarina',
         'São Paulo', 'Sergipe', 'Tocantins', 'Distrito Federal']


#maximizar a tela pela posicao do mouse
posicaoMouse.moveTo(x=876, y=23)
posicaoMouse.click(x=876, y=23)

for estados in lista:
    #Barra de pesquisa
    navegador.find_element(By.XPATH, '/html/body/app/shell/header/busca/div/input').send_keys(estados)
    tempo.sleep(1)
    #clique no estado
    navegador.find_element(By.XPATH, '/html/body/app/shell/header/busca/div/div[2]/div/div[1]/a').click()
    #estado
    print('Estado:', estados)
    tempo.sleep(1)
    #gentilico
    gentilico = navegador.find_element(By.XPATH, '//*[@id="dados"]/panorama-resumo/div/div[1]/div[2]/div/p').text
    print('Gentilico:', gentilico)
    #capital
    capital = navegador.find_element(By.XPATH, '//*[@id="dados"]/panorama-resumo/div/div[1]/div[3]/div/p').text
    print('Capital:', capital)
    #governador
    governador = navegador.find_element(By.XPATH, '//*[@id="dados"]/panorama-resumo/div/div[1]/div[4]/div/p').text
    print('Governador:', governador)
    #populacao estimada
    populacao = navegador.find_element(By.XPATH, '//*[@id="dados"]/panorama-resumo/div/table/tr[2]/td[3]/valor-indicador/div/span[1]').text
    print('População Estimada:', populacao)
    #economia
    economia = navegador.find_element(By.XPATH,'//*[@id="dados"]/panorama-resumo/div/table/tr[38]/th[2]').click()
    tempo.sleep(2)
    #IDH
    idh = navegador.find_element(By.XPATH, '//*[@id="dados"]/panorama-resumo/div/table/tr[41]/td[3]/valor-indicador/div/span[1]').text
    print('IDH:', idh)
    #refresh com a posicao do mouse
    posicaoMouse.moveTo(x=85, y=49)
    posicaoMouse.click(x=85, y=49)
    tempo.sleep(2)
    print('<-------------------------------------------->')

    # Adicionar dados
    linha = planilha_dados.max_row + 1
    colunaA = 'A' + str(linha)
    colunaB = 'B' + str(linha)
    colunaC = 'C' + str(linha)
    colunaD = 'D' + str(linha)
    colunaE = 'E' + str(linha)
    colunaF = 'F' + str(linha)

    # imprimirar os dados na planilha
    planilha_dados[colunaA] = estados
    planilha_dados[colunaB] = gentilico
    planilha_dados[colunaC] = capital
    planilha_dados[colunaD] = governador
    planilha_dados[colunaE] = populacao
    planilha_dados[colunaF] = idh

    # salvando arquivo excel
    workbook.save('Dados.xlsx')


tempo.sleep(5)