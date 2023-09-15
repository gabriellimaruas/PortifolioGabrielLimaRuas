#EXERCÍCIO 2
#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha
#igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir
#as informações.

nome = input('Insira seu nome: ')
senha = input('Insira sua senha: ')

while senha == nome:
    print('Sua senha não pode ser igual ao seu nome.')
    senha = input('Insira uma nova senha: ')

print('Usuário cadastrado.')
print('Seu login é', nome, 'e sua senha é', senha)