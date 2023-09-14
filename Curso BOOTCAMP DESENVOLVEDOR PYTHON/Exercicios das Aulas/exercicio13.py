#Aula 39
#criando uma função de data por extenso
#Crie um programa que apresnete uma data por extenso no formato: cidade,
#99 de XXXXXX de 9999

def data(cidade, dia, mes, ano):
    meses = {1:'Janeiro', 2:'Fevereiro', 3:'Março', 4:'Abril', 5:'Maio',
           6:'Junho', 7:'Julho', 8:'Agosto', 9:'Setembro', 10:'Outubro',
           11:'Novembro', 12:'Dezembro'}
    dt = cidade + ', ' + str(dia) + ' de ' + meses[mes] + ' de ' + str(ano)
    return dt
chamada = data('São Paulo', 5, 5, 2023)
print(chamada)
