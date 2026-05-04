salarios = [1800, 2500, 3200, 4100, 2900]
qtd_salarios = len(salarios)

salarios_ord = sorted(salarios)
print(salarios_ord)
q_aa = salarios_ord[(0)]
q_ab = salarios_ord[(qtd_salarios-1)]

q_b = sum(salarios) / qtd_salarios

q_c = max(salarios)

q_d = []
for sal in salarios:
  if sal > 3000:
    q_d.append(sal)
  else:
    continue

print(q_aa, q_ab)
print(q_b)
print(q_c)
print(q_d)