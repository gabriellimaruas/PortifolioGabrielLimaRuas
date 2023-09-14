#Aula 28
#Crie uma lista de produtos com código, descrição e preço.
#O usuário deverá informar o código para consultar a descrição e o preço do produto.
#O sistema deverá tratar quando informado um código não cadastrado na lista de produtos

#criando uma consulta
produto = {'1': {'descricao' : 'Computador', 'preco': 'R$' + str(10)},
            '2': {'descricao' : 'Monitor', 'preco': 'R$' + str(20)},
            '3': {'descricao' : 'Teclado', 'preco': 'R$' + str(30)}}

codigo = input('Digite o código: ')
if codigo in produto:
    print(produto[codigo]['descricao'], produto[codigo]['preco'])
else:
    print('Código não cadastrado')