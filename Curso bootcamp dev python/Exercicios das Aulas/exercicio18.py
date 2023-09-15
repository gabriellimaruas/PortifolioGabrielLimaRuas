#Aula 44
#Herança

class Pessoa:
    def __init__(self, pNome, pIdade):
        self.nome = pNome
        self.idade = pIdade

    def andar(self):
        print('ANDANDO')

class PessoaFisica(Pessoa):
    #para herdar e n implementar nenhuma característica na classe pessoa, usamos PASS
    pass

pf = PessoaFisica('Anna', 21)

print(pf.nome + ' - ' + str(pf.idade))
pf.andar()


# Para implementar uma caracteristica na classe pessoa
class Pessoa:
    def __init__(self, pNome, pIdade):
        self.nome = pNome
        self.idade = pIdade

    def andar(self):
        print('ANDANDO')

class PessoaFisica(Pessoa):
    def __init__(self, pNome, pIdade, pCPF):
        Pessoa.__init__(self, pNome, pIdade)
        self.cpf = pCPF

class PessoaJuridica(Pessoa):
    def __init__(self, pNome, pIdade, pCNPJ):
        super().__init__(pNome, pIdade)
        self.cnpj = pCNPJ

pf = PessoaFisica('Anna', 21, '123456')
pj = PessoaJuridica('mercado', 2, '78910')

print(pf.nome + ' - ' + str(pf.idade) + ' - ' + pf.cpf)
print(pj.nome + ' - ' + str(pj.idade) + ' - ' + pj.cnpj)

pf.andar()