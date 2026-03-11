
def calc_porc(valor, porc):
  return valor * (porc / 100)

def is_even(num):
  return num % 2 == 0

def is_odd(num):
  return num % 2 != 0

def is_prime(num):
  if num < 2:
    return False
  for x in range(2, int(num**0.5) + 1):
    if (num % x) == 0:
      return False
  return True

def ask_input(msg, type=None):
  entry = None

  type_option = ["int", "float", "string", "char"]

  if type not in type_option:
    print('"type" não identificado')
    return

  while True:
    try:
      print(msg)
      match type:
        case "int":
          entry = int(input("→ "))
        case "float":
          entry = float(input("→ "))
        case "string":
          entry = input("→ ")
        case "char":
          entry = input("→ ")
          if len(entry) != 1:
            raise ValueError
      break
    except ValueError:
      if type == "char":
        print("Digite apenas um caractere!")
      else:
        print("Apenas números!")

  return entry

