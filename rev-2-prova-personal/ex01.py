filmes = [
  {"titulo": "Matrix", "nota": 9.0, "visualizacoes": 1500},
  {"titulo": "Interestelar", "nota": 9.5, "visualizacoes": 2300},
  {"titulo": "Avatar", "nota": 8.0, "visualizacoes": 1800}
]

# a)
for filme in filmes:
  print(filme["titulo"])

# b)
notasB = []
for filme in filmes:
  notasB.append(filme["nota"])
print(max(notasB))

# c)
notasC = []
for filme in filmes:
  notasC.append(filme["nota"])
print(sum(notasC) / len(notasC))

# d)
vizu_boa = []
for filme in filmes:
  if filme["visualizacoes"] > 1700:
    vizu_boa.append(filme)
print(vizu_boa)
