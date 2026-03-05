# Faça um programa que leia o preço de um produto
# e mostre o valor com 5% de desconto.

def ex04():
  print("\n ===== Calculadora de Desconto =====")

  infos = [
    { "label": "Preço do Produto", "value": 0 },
    { "label": "Desconto (em %)", "value": 0 }
  ]

  result = 0

  for info in infos:
    print(f"Entre com {info["label"]}: ")
  
    while True:
      try:
        info["value"] = float(input("→ "))
        break
      except ValueError:
        print("ERROR: Digite apenas números!")
        pass

  result = infos[0]["value"] * ( infos[1]["value"] / 100 )

  for info in infos:
    print(f"{info["label"]}: {info["value"]}")
  
  print(f"Valor com desconto aplicado: {result}")

if __name__ == "__main__":
  ex04()
