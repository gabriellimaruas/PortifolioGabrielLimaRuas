#Aula 35
#Escreva um programa que pergunte ao usuário quantos números de Fibonacci serão gerados e,
#em seguida, imprima os numeros gerados.

# Pede ao usuário o número de números de Fibonacci a serem gerados
num_fibonacci = int(input("Quantos números de Fibonacci você deseja gerar? "))

# Define os dois primeiros números da sequência
fibonacci1 = 0
fibonacci2 = 1

# Imprime os números de Fibonacci gerados
print("Os primeiros", num_fibonacci, "números de Fibonacci são:")

# Loop para gerar e imprimir os números de Fibonacci
for i in range(num_fibonacci):
    # Imprime o número atual da sequência
    print(fibonacci1, end=" ")

    # Calcula o próximo número de Fibonacci
    proximoFibonacci = fibonacci1 + fibonacci2

    # Atualiza os valores dos números de Fibonacci
    fibonacci1 = fibonacci2
    fibonacci2 = proximoFibonacci
