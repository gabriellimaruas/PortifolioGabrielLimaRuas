#SECAO 5
# request e Desafio aula 31
import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.gabrielcasemiro.com.br')
if page.status_code == 200:
    print(page.text)
else:
    print('HTTP error', page.status_code)

soup = BeautifulSoup(page.text)
print(soup)
import pdb; pdb.set_trace()

#####################################################################

import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.gabrielcasemiro.com.br')
if page.status_code == 200:
    soup = BeautifulSoup(page.text)

    for link in soup.find_all('a'):
        print(link.get('href', ''))
else:
    print('HTTP error', page.status_code)


# print(soup)
# import pdb; pdb.set_trace()






