#Aula 43
# Classes e objetos
class MinhaClasse:
    atri1 = 'teste'
    atri2 = 15

obj1 = MinhaClasse()
obj2 = MinhaClasse()

print(obj1.atri1)
print(obj1.atri2)
print(obj2.atri1)
print(obj2.atri2)

# alterando o objeto
class MinhaClasse:
    atri1 = 'teste'
    atri2 = 15

obj1 = MinhaClasse()
obj1.atri1 = 'coisa'
obj1.atri2 = 20

obj2 = MinhaClasse()

print(obj1.atri1)
print(obj1.atri2)
print(obj2.atri1)
print(obj2.atri2)


# Criando classe para inserir valor a um objeto
# init para iniciar
# self = instancia (pode ser outro nome, serve para chamar o parametro dentro da função)
class Aluno:
    def __init__(self, pNome, pIdade):
       self.nome = pNome
       self.idade = pIdade

aluno1 = Aluno('Ana', 21)
aluno2 = Aluno('Ingrid', 20)

print(aluno1.nome)
print(aluno1.idade)

print(aluno2.nome)
print(aluno2.idade)


# exemplo 2
class Aluno:
    def __init__(self, pNome, pIdade, pN1=0, pN2=0, pN3=0):
       self.nome = pNome
       self.idade = pIdade
       self.nota1 = pN1
       self.nota2 = pN2
       self.nota3 = pN3
    def media(self):
        return self.nota3 + self.nota2 + self.nota3 / 4

aluno1 = Aluno('Ana', 21, 70, 80, 90)

print(aluno1.nome)
print(aluno1.idade)
print(aluno1.nota1)
print(aluno1.nota2)
print(aluno1.nota3)
print(aluno1.media())