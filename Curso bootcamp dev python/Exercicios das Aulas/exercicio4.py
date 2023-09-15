#Aula 24
#Criptografia usando o algorítimo Cifra de Cesar
#Escreva um programa Python que criptografa uma senha de 4 digitos.

#criar uma lista alfabética
alfabeto = ['a','b','c','d','e','f','g','h','i','j',
            'k','l','m','n','o','p','q','r','s','t',
            'u','v','w','x','y','z']

r = 3
senha = input('Insira uma senha de 4 letras: ')

#criptografando a senha
d0 = (alfabeto.index(senha[0]) + r) % len(alfabeto)
d1 = (alfabeto.index(senha[1]) + r) % len(alfabeto)
d2 = (alfabeto.index(senha[2]) + r) % len(alfabeto)
d3 = (alfabeto.index(senha[3]) + r) % len(alfabeto)

senha_c = (alfabeto[d0]+alfabeto[d1]+alfabeto[d2]+alfabeto[d3])

#descriptografando a senha para uma verificação

d0 = (alfabeto.index(senha_c[0]) - r) % len(alfabeto)
d1 = (alfabeto.index(senha_c[1]) - r) % len(alfabeto)
d2 = (alfabeto.index(senha_c[2]) - r) % len(alfabeto)
d3 = (alfabeto.index(senha_c[3]) - r) % len(alfabeto)

senha_d=(alfabeto[d0]+alfabeto[d1]+alfabeto[d2]+alfabeto[d3])
print(senha, senha_c, senha_d)


#exemplo de formulas
# r = 3
# i = alfabeto.index('v')
# #index criptografado (formula) para criptografar
# i_c = (i + r) % len(alfabeto)
# #index descriptografado para descriptografar
# i_d = (i_c - r) % len(alfabeto)
#
# print(i,alfabeto[i],i_c,alfabeto[i_c], i_d)