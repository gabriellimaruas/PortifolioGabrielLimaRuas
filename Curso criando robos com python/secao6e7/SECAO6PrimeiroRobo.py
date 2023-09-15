#secao 6
#primeiro robo
import xlrd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

print('Iniciando nosso robô...\n')

driver = webdriver.Chrome()
driver.get('https://registro.br/')

dominios = ['roboscompython.com.br', 'annavoeg.com.br', 'uol.com.br', 'vaicorinthians.com.br']

for dominio in dominios:
    pesquisa = driver.find_element(By.ID, 'is-avail-field')  # achando a barra de pesquisa
    pesquisa.clear()  # limpando a barra de pesquisa
    pesquisa.send_keys(dominio)#escrevendo na barra
    pesquisa.send_keys(Keys.RETURN)#tecla enter
    time.sleep(2)
    resposta = driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div/section/div[2]/div/p').text #pegando a resposta do site
    print(dominio, '=', resposta)
    time.sleep(0)

time.sleep(3)
driver.close()
