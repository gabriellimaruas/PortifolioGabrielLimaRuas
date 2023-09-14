#Aula 48
#CRUD/ESTOQUE/MENU
#Alterar o programa de estoque para permitir interação com usuário.
#Crie um menu de opções e permita ao usuário entrar com os dados.

import os

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

sair = False

while not sair:
    #comando para limpar o terminal, porém não funcionou na minha máquina
    os.system('cls')

    print('''
    +-------------------------------+
    |       SISTEMA DE ESTOQUE      |
    +-------------------------------+
    |              MENU             |
    +-------------------------------+
    |           (I) Incluir         |
    |           (A) Alterar         |
    |           (E) Excluir         |
    |           (L) Listar          |
    |           (S) Sair            |
    +-------------------------------+
            ''')

    op = input('Selecione uma opcao: ').upper()

    if op == 'S':
        sair = True
    elif op == 'I':
        codigo = input('Digite o código: ')
        descricao = input('Digite a descrição: ')
        preco = input('Digite o preço: ')
        e.incluir(codigo, descricao, preco)
        print('INCLUÍDO')
        input('<ENTER> para continuar')
    elif op == 'A':
        codigo = input('Digite o código: ')
        preco = input('Digite o preço: ')
        e.alterar(codigo, preco)
        print('ALTERADO')
        input('<ENTER> para continuar')
    elif op == 'E':
        codigo = input('Digite o código: ')
        e.excluir(codigo)
        print('EXCLUÍDO')
        input('<ENTER> para continuar')
    elif op == 'L':
        e.listar()
        input('<ENTER> para continuar')

print('Fim do sistema, obrigado!')