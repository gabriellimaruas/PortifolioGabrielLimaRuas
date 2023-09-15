#secao 5
#exercicios resolvidos
from bs4 import BeautifulSoup
html_file = open('arquivosS5/data_in_table.html', mode='r', encoding='utf-8')

soup = BeautifulSoup(html_file, 'html.parser')
table = soup.find(id='main_table')
table_rows = table.find_all('tr')

# print(table_rows)

dados_alunos = []

for linha in table_rows:
    colunas = linha.find_all('td')
    if len(colunas) > 0:
        codigo_estudante = colunas[0].text
        nome_estudante = colunas[1].text
        nota_estudante = colunas[2].text
        dict_aluno = {
            'codigo': codigo_estudante,
            'nome': nome_estudante,
            'nota': nota_estudante
        }
        dados_alunos.append(dict_aluno)
        print(f'{codigo_estudante} - {nome_estudante} - {nota_estudante}')

print(dados_alunos)
#execucao para no final do script e da para interagir com o script
import pdb; pdb.set_trace()

########################################################################################################################

from bs4 import BeautifulSoup
#abrir o arquivo html
html_file = open('arquivosS5/data_in_table_2.html', mode='r', encoding='utf-8')
#usa o BeautifulSoup para extrair as informações
soup = BeautifulSoup(html_file, 'html.parser')
#encontrar todas as tabelas e escolher a segunda
table = soup.find_all('table')[1]
#escolher todas as linhas
table_rows = table.find_all('tr')
print(table_rows)

#faz uma lista para armazenas os dados
dados_cursos = []

#percorre todas as linhas encontrando todas as colunas
for linha in table_rows:
    colunas = linha.find_all('td')
    #se tiver mais de uma coluna, ele extrai os dados nome e interesse
    if len(colunas) > 0:
        nome_curso = colunas[0].text
        interesse = colunas[1].text
        #estrutura os dados em um dicionario
        dict_curso = {'nome': nome_curso, 'interesse': interesse}
        #coloca dentro da lista
        dados_cursos.append(dict_curso)

print(dados_cursos)
import pdb; pdb.set_trace()


