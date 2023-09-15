#Aula 49
#Escreva uma classe Python chamada Retangulo composta pelo comprimento, largura
#e um método que irá calcular a área de um retângulo.

class Retangulo():
    def __init__(self, comprimento, largura):
        self.comprimento = int(input('Digite o comprimento do retângulo:'))
        self.largura = int(input('Digite a largura do retângulo:'))

    def calcArea(self):
        return self.largura * self.comprimento

objRet = Retangulo('comprimento','largura')
print(objRet.calcArea())