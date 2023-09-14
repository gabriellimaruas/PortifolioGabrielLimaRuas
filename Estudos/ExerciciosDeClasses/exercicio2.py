#EXERCÍCIO 2
#Classe Quadrado: Crie uma classe que modele um quadrado:
#Atributos: Tamanho do lado
#Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado():
    def __init__(self, lado):
        self.lado = lado

    def mudar(self, lado2):
        self.lado = lado2

    def retornoLado(self):
        return self.lado

    def calcArea(self):
        area = self.lado ** 2
        return area

quadrado1 = Quadrado(int(input('Digite a medida do quadrado em cm: ')))
print('A área do quadrado é de',quadrado1.calcArea(),'cm')

quadrado1.mudar(int(input('Digite a nova medida do quadrado em cm: ')))
print('A nova área do quadrado é de',quadrado1.calcArea(),'cm')