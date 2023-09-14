#Aula 27
#loop if e else
#nota de um aluno

#if e else básico de nota
nota = int(input("insira sua nota: "))
print(type(nota))

if nota >= 70:
    print("Parabéns, você passou!")
else:
    print("Reprovado!")


#if e else para saber se a nota é A, B, C...
nota = int(input('Insira sua nota: '))
if nota >= 90:
    print('Sua nota é A')
    print('Parabéns, Você passou!')
elif nota >= 80:
    print('Sua nota é B')
    print('Parabéns, Você passou!')
elif nota >= 70:
    print('Sua nota é C')
    print('Parabéns, Você passou!')
else:
    print('Infelizmente você foi reprovado!')