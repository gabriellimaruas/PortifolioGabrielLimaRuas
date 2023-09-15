#secao 7
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

pesquisa = input('Digite o que deseja pesquisar: ')

driver = webdriver.Chrome()

driver.get('http://www.google.com')

# achando a barra de pesquisas
campo = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
#escrevendo na barra de pesquisas o que pedir na variavel pesquisa
campo.send_keys(pesquisa)
#tecla enter
campo.send_keys(Keys.ENTER)

#achando a quantidade de resultados
#XPATH da quantidade de resultados //*[@id="result-stats"]
resultado = driver.find_element(By.XPATH, '//*[@id="result-stats"]').text
print(resultado)

#recuperando o numero de paginas
numeroResultado = int(resultado.split('Aproximadamente ')[1].split(' resultados')[0].replace('.', ''))
#Cada pagina tem 10 links, então dividiremos o resultado por 10
maximoPaginas = numeroResultado/10
print('Número de páginas: %s' % maximoPaginas)

#navegando entre as paginas do google
urlPagina = driver.find_element(By.XPATH, '//*[@id="botstuff"]/div/div[3]/table/tbody/tr/td[3]/a').get_attribute('href')

pagAtual = 0
start = 10
while pagAtual <= 10:
    if not pagAtual == 0:
        url = urlPagina.replace('start=%s' % start, 'start=%s' % (start + 10))
        start += 10
    pagAtual += 1
    driver.get(urlPagina)

time.sleep(1000)






#    Corinthians