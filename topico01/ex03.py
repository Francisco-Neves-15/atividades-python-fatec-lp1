# Supondo que queremos pintar o muro da instituição, faça um programa
# que leia a altura e a largura do muro e mostre a quantidade de tinta
# necessária (1 litro de tinta pode pintar uma área de 2 metros quadrados).

def ex03():
  print("\n ===== Calculadora de Pintar Muros =====")

  infos = [
    { "label": "Altura", "value": 0 },
    { "label": "Largura", "value": 0 }
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

  result = ( infos[0]["value"] * infos[1]["value"] ) / 2

  for info in infos:
    print(f"{info["label"]}: {info["value"]}")
  
  print(f"Baldes de tinta necessários: {result}")

if __name__ == "__main__":
  ex03()
