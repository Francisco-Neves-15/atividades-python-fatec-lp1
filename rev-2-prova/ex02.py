produtos = {
  "p1": ("Teclado", 120.0, 5),
  "p2": ("Mouse", 80.0, 10),
  "p3": ("Monitor", 900.0, 2)
}

q_a = 0
for nome, preco, quantidade in produtos.values():
  q_a += preco * quantidade

precos = []
for nome, preco, quantidade in produtos.values():
  precos.append(quantidade)
q_b = max(precos)

q_c = 0
for nome, preco, quantidade in produtos.values():
  q_c += quantidade

q_d = []
for nome, preco, quantidade in produtos.values():
  q_d.append(nome)

print(q_a)
print(q_b)
print(q_c)
print(q_d)