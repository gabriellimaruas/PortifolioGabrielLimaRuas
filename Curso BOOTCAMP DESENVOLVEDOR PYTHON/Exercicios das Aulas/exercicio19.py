#Aula 45

#Polimorfismo
#mesma função mas opera diferente
print(len('olá mundo'))
print(len([1,2,3]))

# Polimorfismo com classes
class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def calc(self):
        return self.x + self.y

class B:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):
        return self.x * self.y

a = A(10, 5)
print(a.calc())
b = B(10, 5)
print(b.calc())

# Polimorfismo com classes e herança
class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def calc(self):
        return self.x + self.y

class B:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):
        return self.x * self.y

class C(A):
    def __init__(self, x, y):
        super().__init__(x, y)

    def calc(self):
        return self.x - self.y

c = C(10, 50)
print(c.calc())