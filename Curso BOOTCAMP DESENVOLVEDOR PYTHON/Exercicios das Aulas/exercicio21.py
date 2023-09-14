#Aula 47
#Crie um programa para incluir, excluir, alterar e listar itens de estoque. Os dados a serem gravados
#são código, descrição e preço. No caso da alteração o programa altera apenas o preço do produto.

#estoque class
class Estoque:
    itens = {}
#metodo para incluir
    def incluir(self, codigo, desc, preco):
        if codigo not in self.itens:
            self.itens[codigo] = {'descricao':desc, 'preco':preco}
        else:
            print('Código já cadastrado')

#metodo alterar
    def alterar(self, codigo, preco):
        if codigo in self.itens:
            self.itens[codigo]['preco']=preco
        else:
            print('Código não existe')

#metodo excluir
    def excluir(self, codigo):
        if codigo in self.itens:
            self.itens.pop(codigo)
        else:
            print('Código não existe')

#metodo listar
    def listar(self):
        print('---------------------------------------')
        for codigo in self.itens:
            print(codigo, self.itens[codigo]['descricao'], self.itens[codigo]['preco'])
        print('---------------------------------------')

e = Estoque()
#incluindo
e.incluir('x01', 'Computador', 750)
e.incluir('x02', 'Monitor', 1500)
e.incluir('x03', 'Teclado', 500)
#listando
e.listar()
#alterando
e.alterar('x02', 1300)
e.listar()
#excluindo
e.excluir('x02')
e.listar()