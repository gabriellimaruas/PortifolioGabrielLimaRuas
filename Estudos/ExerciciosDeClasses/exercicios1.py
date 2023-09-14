#EXERCÍCIO 1
#Classe Bola: Crie uma classe que modele uma bola:
#Atributos: Cor, circunferência, material
#Métodos: trocaCor e mostraCor

class Bola():
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor
    def mostrarCor(self):
        print(self.cor)

bola1 = Bola(input('Insira a cor da bola: '),input('Insira a cincunferência da bola: '),
             input('Insira o material da bola: '))

bola1.mostrarCor()
bola1.trocaCor(input('Insira a nova cor: '))
bola1.mostrarCor()