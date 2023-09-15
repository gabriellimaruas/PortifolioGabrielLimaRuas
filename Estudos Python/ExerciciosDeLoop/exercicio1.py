#EXERCÍCIO 1
#Faça um programa que peça uma nota, entre zero e dez.
#Mostre uma mensagem caso o valor seja inválido e continue pedindo
#até que o usuário informe um valor válido.

nota = float(input('Insira sua nota: '))
while (nota > 10) or (nota < 0):
    print('Nota inválida, sua nota deve ser entre 0 e 10')
    nota = float(input('Tente novamente:'))
print('Nota válida')