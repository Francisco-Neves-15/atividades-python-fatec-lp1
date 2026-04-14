# Faça um programa que crie dois conjuntos x e y,
# com dez números inteiros cada um. Em seguida, crie:
# 1) Um conjunto resultante da união de x e y (todos os
# elementos de x e os elementos de y que não estão em x).
# 2) Um conjunto resultante da diferença entre x e y (todos
# os elementos de x que não existam em y).
# 3) Um conjunto resultante interseção entre x e y

x = {1, 2, 3, 4, 5, 7, 8, 9, 10}
y = {8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18}

uniao = x | y
inter = x & y
dif = x - y

print(uniao)
print(inter)
print(dif)