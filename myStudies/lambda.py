root = lambda num, rad: num ** ( 1 / rad )
delta = lambda a, b, c: (b**2) - (4*a*c)
bhaskara = lambda a, b, c: [
  -b + root(delta(a, b, c), 2) / (2*a),
  -b - root(delta(a, b, c), 2) / (2*a),
]
print(bhaskara(1,-5,6))