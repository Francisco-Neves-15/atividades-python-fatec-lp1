alunos = [
  ("Marcos", 7.5),
  ("Fernanda", 9.0),
  ("Lucas", 5.5),
  ("Amanda", 8.0)
]

# a)
print(alunos[0][0], alunos[0][1])

# b)
somaB = 0
qtdB = 0
for nome, nota in alunos:
  somaB += nota
  qtdB += 1
print(somaB / qtdB)

# c)
maior = ("", 0)
for nome, nota in alunos:
  if nota > maior[1]:
    maior = (nome, nota)
print(maior)

# d)
aprovados = []
for nome, nota in alunos:
  if nota >= 7:
    aprovados.append((nome, nota))
print(aprovados)
