# Escreva um algoritmo que permita a leitura das notas de uma turma de 20 alunos. Calcular a média da turma e contar quantos alunos obtiveram nota acima desta média calculada. Escrever a média da turma e o resultado da contagem.

# Inicialize uma lista vazia para armazenar as notas dos alunos
notas = []

# Faça um loop para ler as notas dos 20 alunos
for i in range(20):
    nota = float(input(f'Digite a nota do aluno {i + 1}: '))
    notas.append(nota)

# Calcule a média da turma
media_turma = sum(notas) / len(notas)

# Inicialize um contador para contar quantos alunos obtiveram notas acima da média
acima_da_media = 0

# fazer um loop para verificar as notas e contar os alunos acima da média
for nota in notas:
    if nota > media_turma:
        acima_da_media += 1

# Exiba a média da turma e o resultado da contagem
print(f'Média da turma: {media_turma:.2f}')
print(f'Número de alunos acima da média: {acima_da_media}')
