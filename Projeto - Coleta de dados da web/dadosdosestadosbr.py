from selenium import webdriver as bot
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# imports excel
from openpyxl import Workbook
import os
# import para a fonte e alinhamento
from openpyxl.styles import Font, Alignment

# Funcao para definir o estilo dos titulo para a planilha
def configurar_titulos_estilos(planilha):
    # Definir a coluna, largura e o titulo das celulas
    largura_titulos = {
        'A': (21, 'Estado'),
        'B': (51, 'Gentílico'),
        'C': (21, 'Capital'),
        'D': (45, 'Governador'),
        'E': (23, 'Pop. Estimada'),
        'F': (20, 'IDH')
    }

    # Loop para adicionar os titulos na planilha
    for coluna, (largura, titulo) in largura_titulos.items():
        planilha.column_dimensions[coluna].width = largura
        celula_largura_titulo = planilha[f'{coluna}1']
        celula_largura_titulo.value = titulo

    # Definir o estilo das celulas com titulo
    estilo_titulo = Font(bold=True, size=14)
    alignment_titulo = Alignment(horizontal='center', vertical='center')

    # Listar as linhas e colunas que serao modificadas
    celula_titulo = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1']

    # Loop para aplicar os estilos nas celulas
    for estilos in celula_titulo:
        celula_estilo_titulo = planilha[estilos]
        celula_estilo_titulo.font = estilo_titulo
        celula_estilo_titulo.alignment = alignment_titulo

# funcao para coleta de dados e manipular estilo dos dados
def tentativa_coleta_dados(navegador, estado):
    tentativas = 3

    for tentativa in range(1, tentativas + 1):
        try:
            # gentilico
            gentilico = navegador.find_element(By.XPATH, '//*[@id="dados"]/panorama-resumo/div/div[1]/div[2]/div/p').text
            # capital
            capital = navegador.find_element(By.XPATH, '//*[@id="dados"]/panorama-resumo/div/div[1]/div[3]/div/p').text
            # governador
            governador = navegador.find_element(By.XPATH, '//*[@id="dados"]/panorama-resumo/div/div[1]/div[4]/div/p').text
            # populacao estimada
            populacao = navegador.find_element(By.XPATH, '//*[@id="dados"]/panorama-resumo/div/table/tr[2]/td[3]/valor-indicador/div/span[1]').text
            # economia
            economia = navegador.find_element(By.XPATH,'//*[@id="dados"]/panorama-resumo/div/table/tr[38]/th[2]').click()
            time.sleep(1)
            # IDH
            idh = navegador.find_element(By.XPATH, '//*[@id="dados"]/panorama-resumo/div/table/tr[41]/td[3]/valor-indicador/div/span[1]').text
            # Botao populacao
            botao_populacao = navegador.find_element(By.XPATH, '//*[@id="dados"]/panorama-resumo/div/table/tr[1]/th[2]').click()
            time.sleep(1)

            # print dos dados
            print('Estado: ', estado)
            print('Gentilico: ', gentilico)
            print('Capital: ', capital)
            print('Governador: ', governador)
            print('População Estimada:', populacao, 'pessoas')
            print('IDH: ', idh)

            print('<-------------------------------------------->')

            # Definir colunas, dados e fonte das celulas dos dados
            colunas_dados = ['A', 'B', 'C', 'D', 'E', 'F']
            dados_coletados = [estado, gentilico, capital, governador, populacao, idh]
            fonte_dados = Font(size=12)

            # Interar os dados na planilha
            linha = planilha_dados.max_row + 1

            # loop para adicionar os dados a planilha
            for coluna_exata, dado_exato in zip(colunas_dados, dados_coletados):
                celula_exata = coluna_exata + str(linha)

                # verificar se é a coluna populacao para adicionar o populacao_pessoas
                if coluna_exata == 'E':
                    planilha_dados[celula_exata] = f'{populacao} pessoas'
                else:
                    planilha_dados[celula_exata] = dado_exato
                planilha_dados[celula_exata].font = fonte_dados
            break

        except Exception as e:
            print(f'Tentativa {tentativa} de coleta de dados do estado {estado} falhou: {e}')

        if tentativa < tentivas:
            print(f'Tentativa {tentativa} de {tentativas}. Tentando novamente...')
        else:
            print(f'Atingido o número máximo de tentativas para {estado}. Desculpe.')

# Criar, ativar e definir titulo da pag da planilha excel
workbook = Workbook()
planilha_dados = workbook.active
planilha_dados.title = 'DADOS'

# Chamar a função configurar_titulos_estilos para ser executada na planilha_dados
configurar_titulos_estilos(planilha_dados)

# Iniciar bot selenium e maximizar janela
print('Abrindo navegador, um momento...')
navegador = bot.Chrome()
navegador.get('https://cidades.ibge.gov.br/')
navegador.maximize_window()

# Lista de estados a terem os dados coletados
lista_estados = ['Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 'Espírito Santo', 'Goiás', 'Maranhão',
         'Mato Grosso', 'Mato Grosso Do Sul', 'Minas Gerais', 'Pará', 'Paraíba', 'Paraná', 'Pernambuco', 'Piauí',
         'Rio de Janeiro', 'Rio Grande Do Norte', 'Rio Grande Do Sul', 'Rondônia', 'Roraima', 'Santa Catarina',
         'São Paulo', 'Sergipe', 'Tocantins', 'Distrito Federal']

# Loop para coleta de dados
for estado in lista_estados:
    time.sleep(2)
    # Barra de pesquisa
    barra_pesquisa = navegador.find_element(By.CSS_SELECTOR, 'body > app > shell > header > busca > div > input')
    barra_pesquisa.send_keys(estado)
    time.sleep(1)
    
    # Clique no estado
    clique_estado = navegador.find_element(By.CSS_SELECTOR, 'body > app > shell > header > busca > div > div.busca__auto-completar > div > div:nth-child(1) > a')
    clique_estado.click()
    time.sleep(2)

    print(f'Coletando os dados do estado {estado}, um momento...')

    # Chamar a funcao tentativa_coleta_dados
    tentativa_coleta_dados(navegador, estado)

    # Salvar o arquivo
    workbook.save('Dados.xlsx')

print('Finalizando robô...')
time.sleep(1)
navegador.quit()
print('Robô Finalizado!')
