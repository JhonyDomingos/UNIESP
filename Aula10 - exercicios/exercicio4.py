# iniciar um vetor vazio para armazenar os números de A
A = []

# fazer um loop para ler os 10 números de A
for i in range(10):
    numero = float(input(f'Digite o número {i + 1} de A: '))
    A.append(numero)

# Leia o número X
X = float(input('Digite o número X: '))

# iniciaar um vetor vazio para armazenar os resultados da multiplicação
M = []

# fazer um loop para multiplicar cada elemento de A por X e armazenar em M
for numero in A:
    resultado = numero * X
    M.append(resultado)

# exibir o vetor M
print('O vetor M é:', M)
