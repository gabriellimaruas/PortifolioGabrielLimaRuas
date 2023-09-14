#Aula 50
#Crie uma classe chamada Restaurante. O método __init __ () para o restaurante
#deve armazenar dois atributos: nome e cozinha. Crie um método chamado desc()
#que imprime esses dois atributos, e um método chamado abrir() que imprime uma
#mensagem indicando que o restaurante está aberto.

#Crie uma instância chamada obRest da sua classe. Imprima os dois atributos
#individualmente e, em seguida, chame os dois métodos.


class Restaurante():
    def __init__(self):
        self.nome = input('Digite nome do seu Restaurante: ')
        self.cozinha = input('Digite o tipo do seu Restaurante: ')
#metodo desc() para imprimir nome cozinha
    def desc(self):
        print('O restaurante', self.nome , 'é do tipo ', self.cozinha)

#metodo abrir() que imprime uma msg indicando que o restaurante está aberto
    def abrir(self):
        print('O restaurante', self.nome ,'está aberto')

#Instancia objRest para imprimir os dois atributos individualmente
objRest = Restaurante()

objRest.desc()
objRest.abrir()