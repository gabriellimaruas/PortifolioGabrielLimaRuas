#secao 5
#Beautiful Soup
from bs4 import BeautifulSoup
html_file = open('arquivosS5/generic_simple.html', mode='r', encoding='utf-8')
# print(html_file)

soup = BeautifulSoup(html_file, 'html.parser')
print(soup)
print(dir(soup))
print(soup.prettify())
print(soup.get_text())
print(soup.title)
print(soup.title.name)
print(soup.title.parent)
print(soup.title.parent.name)
print(soup.title.parent.parent.name)
print(soup.div)
print(list(soup.div.children))
for i in list(soup.div.children):
    print(i.name)
# pegar primeira string
print(soup.p.string)
# pegar o primeiro link
print(soup.a)
# pegar somente o link
print(soup.a['href'])


# Outra forma de pegar os dados é usando o .find(define oq quer pegar)
print(soup.find('div'))
print(soup.find('div', id='imp_article_ID'))
# para pegar pela classe
print(soup.find_all('div', class_='article')[0])
print(soup.find_all('div', class_='article')[1])
print(soup.find_all('div', class_='article')[2])










