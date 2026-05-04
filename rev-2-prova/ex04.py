livros = {
  "Livro A": 5,
  "Livro B": 2,
  "Livro C": 0
}

q_a = list(livros.keys())
q_b = livros["Livro C"] > 0
q_c = sum(list(livros.values()))
q_d = []
for nome, qtd in livros.items():
  q_d.append(nome) if qtd > 0 else None

print(q_a)
print(q_b)
print(q_c)
print(q_d)