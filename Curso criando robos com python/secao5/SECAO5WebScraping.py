#secao 5
#WebScraping
from bs4 import BeautifulSoup
html_file = open('arquivosS5/data_in_table.html', mode='r', encoding='utf-8')

soup = BeautifulSoup(html_file, 'html.parser')
table = soup.find(id='main_table')
table_rows = table.find_all('tr')

print(table_rows)


