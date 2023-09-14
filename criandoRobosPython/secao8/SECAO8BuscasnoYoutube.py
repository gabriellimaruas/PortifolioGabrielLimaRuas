import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class RoboYoutube():
    def __init__(self):
        self.webdriver = webdriver.Chrome()
        self.webdriver.maximize_window()

    def busca(self, busca, paginas):
        videos = []
        pagina = 1

        url = 'https://www.youtube.com/results?search_query=%s' % busca
        self.webdriver.get(url)

        while pagina <= paginas:
            titulos = self.webdriver.find_elements(By.XPATH, '//a[@id="video-title"]')
            for titulo in titulos:
                if titulo.text not in videos:
                    print('Vídeo encontrado: %s' % titulo.text)
                    videos.append(titulo.text)
            self.proximaPagina(pagina)
            pagina += 1

    def proximaPagina(self, pagina):
        print('Mudando para a página %s' % (pagina + 1))
        bottom = pagina * 10000
        self.webdriver.execute_script('window.scrollTo(0, %s);' % bottom)
        time.sleep(5)
        pass


bot = RoboYoutube()
bot.busca('valorant', 5)

