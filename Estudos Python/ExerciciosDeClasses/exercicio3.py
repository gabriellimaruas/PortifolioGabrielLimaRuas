#EXERCÍCIO 3
#Classe Pessoa: Crie uma classe que modele uma pessoa:
#Atributos: nome, idade, peso e altura
#Métodos: Envelhercer, engordar, emagrecer, crescer.
#Obs: Por padrão, a cada ano que nossa pessoa envelhece,
#sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa():
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        self.idade += anos
        if self.idade < 21:
            self.crescer(0.5)

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura

# Solicita as informações iniciais ao usuário
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura em metros (ex. 1.70): '))

pessoa1 = Pessoa(nome, idade, peso, altura)

print('---------------------------------------------')

anos_para_envelhecer = int(input('Quantos anos deseja envelhecer: '))
pessoa1.envelhecer(anos_para_envelhecer)

print('Ao envelhecer', anos_para_envelhecer, 'anos, você terá', pessoa1.idade, 'anos de idade e', pessoa1.altura, 'metros de altura')
print('Peso atual:', pessoa1.peso, 'Kg')

quilos_para_engordar = float(input('Digite o quanto deseja engordar: '))
pessoa1.engordar(quilos_para_engordar)
print('Ao engordar', quilos_para_engordar, 'Kg, você terá', pessoa1.peso, 'Kg')

quilos_para_emagrecer = float(input('Digite o quanto deseja emagrecer: '))
pessoa1.emagrecer(quilos_para_emagrecer)
print('Ao emagrecer', quilos_para_emagrecer, 'Kg, você terá', pessoa1.peso, 'Kg')