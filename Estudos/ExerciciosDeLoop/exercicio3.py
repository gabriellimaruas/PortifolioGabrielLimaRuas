#EXERCÍCIOS 3
# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';
# Use a função len(string) para saber o tamanho de um texto (número de caracteres).

nome = input('Insira seu nome: ')
idade = int(input('Insira sua idade: '))
salario = float(input('Insira seu salário: '))
sexo = input('Insira seu sexo (F)emea, (M)acho: ').lower()
estCivil = input('Insira seu estado civil (S)olteiro, (C)asado,\n'
                  '(V)iuva(o), (D)ivorciada(o): ').lower()

while len(nome) <= 3:
    nome = input('Nome inválido, insira um nome com mais de 3 letras: ')
print('Nome válido')

while idade < 0 or idade > 150:
    idade = int(input('Idade inválida, insira uma idade entre 0 e 150: '))
print('Idade válida')

while salario < 0:
    salario = float(input('Salário inválido, insira um sálario maior que 0: '))
print('Salário válido')

while estCivil != 's' and estCivil != 'c' and estCivil != 'v' and estCivil != 'd':
    estCivil = input('Estado civil inválido, insira um estado civil (S)olteiro,\n '
                     '(C)asado,(V)iuva(o), (D)ivorciada(o): ').lower()
print('Estado civil válido')