salarios = [1800, 2500, 3200, 4100, 2900]

salarios.sort()
print(salarios)
q_aa = salarios[0]
q_ab = salarios[-1]

q_b = sum(salarios) / len(salarios)

q_c = max(salarios)

q_d = []
for sal in salarios:
  if sal > 3000:
    q_d.append(sal)

print(q_aa, q_ab)
print(q_b)
print(q_c)
print(q_d)