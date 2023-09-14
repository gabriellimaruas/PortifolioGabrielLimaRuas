# Aula 18
# Criando um pedido de compra
# Escreva um programa que simule um pedido de compra. O usuário
# deverá informar seu CPF,Nome, Código do Produto, Qtde e Valor.
# O sistema deverá então imprimir os dados informados.

cpf = input('CPF: ')
nome = input('Nome: ')
codigo = input('Código do produto: ')
qtde = input('Quantidade :')
valor = input('Valor :')

print('===============================================')
print(">>> Dados do pedido <<<")
print('===============================================')
print('CPF informado: '+cpf)
print('Nome informado: '+nome)
print('Código informado: '+codigo)
print('Quantidade informada: '+qtde)
print('Valor informado: R$'+valor)
print('===============================================')