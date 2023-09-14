#SECAO 10
#GRAFICOS 2D

from openpyxl import Workbook
import os
from openpyxl.chart import (
    AreaChart,
    Reference,
    AreaChart3D
)

wb = Workbook()
ws = wb.active

rows = [
    ['Ano', 'Lucros', 'Custos'],
    [2015, 40, 30],
    [2016, 40, 25],
    [2017, 45, 25],
    [2018, 50, 30],
    [2019, 30, 10],
    [2020, 25, 5]
]

for row in rows:
    ws.append(row)

#Criando grafico 2D
chart = AreaChart()
chart.title = 'Lucros x Custos'
chart.style = 13
chart.x_axis.title = 'Ano'
chart.y_axis.title = 'Porcetagem'

categorias = Reference(ws, min_col=1, min_row=1, max_row=6)
dados = Reference(ws, min_col=2, min_row=1, max_col=3, max_row=6)

chart.add_data(dados, titles_from_data=False)
chart.set_categories(categorias)

ws.add_chart(chart, 'A10')


wb.save('Chart2D.xlsx')
os.startfile('Chart2D.xlsx')


#GRAFICOS 3D
wb = Workbook()
ws = wb.active

rows = [
    ['Ano', 'Lucros', 'Custos'],
    [2015, 30, 40],
    [2016, 25, 40],
    [2017, 30, 50],
    [2018, 10, 30],
    [2019, 5, 25],
    [2020, 10, 50]
]

for row in rows:
    ws.append(row)

#Criando grafico 2D
chart = AreaChart3D()
chart.title = 'Lucros x Custos'
chart.style = 13
chart.x_axis.title = 'Ano'
chart.y_axis.title = 'Porcetagem'

categorias = Reference(ws, min_col=1, min_row=1, max_row=6)
dados = Reference(ws, min_col=2, min_row=1, max_col=3, max_row=6)

chart.add_data(dados, titles_from_data=True)
chart.set_categories(categorias)

ws.add_chart(chart, 'A10')


wb.save('Chart3D.xlsx')
os.startfile('Chart3D.xlsx')




