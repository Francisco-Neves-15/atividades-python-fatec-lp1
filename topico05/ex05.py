# Pangrama, ou pantograma, (do grego, pan ou
# pantós = todos, + grama = letra) é uma frase 
# em que são usadas todas as letras do alfabeto 
# de determinada língua. A partir da definição, 
# crie um código python para definir se uma frase 
# é ou não um pangrama.
# https://pt.wikipedia.org/wiki/Pangrama

import string

alfabeto = string.ascii_lowercase

# Use como exemplo a frase:
frase1 = 'Jane quer LP, fax, CD, giz, TV e bom whisky'
frase2 = 'Pneumoultramicroscopticosilicovulcanoconiotico'

frase1_set = set()
frase2_set = set()

for l in frase1:
  l = l.lower()
  if l.isalpha():
    frase1_set.add(l)
frase1_set = sorted(frase1_set)

for l in frase2:
  l = l.lower()
  if l.isalpha():
    frase2_set.add(l)
frase2_set = sorted(frase2_set)

frase1_set = "".join(frase1_set)
frase2_set = "".join(frase2_set)

if (frase1_set == alfabeto):
  print("É um pantograma")
else:
  print("Não é um pantograma")

if (frase2_set == alfabeto):
  print("É um pantograma")
else:
  print("Não é um pantograma")
