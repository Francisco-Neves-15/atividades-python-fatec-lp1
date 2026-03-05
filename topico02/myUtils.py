class myUtils:
  @staticmethod
  def calc_porc(valor, porc):
    return valor * (porc / 100)

  @staticmethod
  def ask_input(msg, type=None):
    entry = None

    type_option = ["int", "float", "string"]

    if type not in type_option:
      return print('"type" não identificado')

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
        break
      except ValueError:
        print("Apenas números!")
        pass
  
    return entry
