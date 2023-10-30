# Escreva um algoritmo que permita a leitura dos nomes de 10 clubes de futebol e armazene os nomes lidos em um vetor (lista). Após isto, o algoritmo deve permitir a leitura de mais 1 nome qualquer de clube e depois escrever a mensagem ACHEI, se o nome estiver entre os 10 nomes lidos anteriormente (guardados no vetor), ou NÃO ACHEI caso contrário.

# inicializar uma lista vazia para armazenar os nomes dos clubes
clubes = []

# fazer um loop para ler os nomes dos clubes
#usando o lower case para pode ignorar o case sensitive 
for i in range(10):
    nome_clube = input(f'Digite o nome do clube {i + 1}: ').lower()
    clubes.append(nome_clube)

# Leia o nome para verificar
nome_verificar = input('Agora, digite um nome de clube para verificar se existe na lista: ').lower()

# verificar se o nome está na lista e exiba a mensagem apropriada
if nome_verificar in clubes:
    print('ACHEI')
else:
    print('NÃO ACHEI')
