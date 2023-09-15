#Aula 19
#Calculando o total do pedido de compra
#Altere o program pedido de compra para que o possa ser informado
#3 produtos. Quando os dados forem impressos mostre o total do pedido.

cpf = input('CPF: ')
nome = input('Nome: ')
c1 = input('Código do produto: ')
q1 = input('Quantidade :')
v1 = input('Valor :')
c2 = input('Código do produto: ')
q2 = input('Quantidade :')
v2 = input('Valor :')
c3 = input('Código do produto: ')
q3 = input('Quantidade :')
v3 = input('Valor :')

print('===============================================')
print(">>> Dados do item 1 <<<")
print('CPF informado: '+cpf)
print('Nome informado: '+nome)
print('Código informado: '+c1)
print('Quantidade informada: '+q1)
print('Valor informado: R$'+v1)

print('===============================================')
print(">>> Dados do item 2 <<<")
print('Código informado: '+c2)
print('Quantidade informada: '+q2)
print('Valor informado: R$'+v2)

print('===============================================')
print(">>> Dados do item 3 <<<")
print('Código informado: '+c3)
print('Quantidade informada: '+q3)
print('Valor informado: R$'+v3)

total = (int(q1)*float(v1)) + (int(q2)*float(v2)) + (int(q3)*float(v3))

print('===============================================')
print(">>> TOTAL DO PEDIDO <<<")
print('Total do pedido: R$'+ str(total))