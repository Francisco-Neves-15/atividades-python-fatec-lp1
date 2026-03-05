# Faça um programa para aprovar o empréstimo bancário para
# a compra de uma casa. O usuário deverá informar o valor
# da casa, a quantidade de parcelas que deseja pagar e seu
# salário. O empréstimo deverá ser negado caso o valor da
# parcela exceda 30% do salário.

from myUtils import myUtils

def main():
  print("\n===== Empréstimo Bancário =====")

  PORC_EXCED = 30
  valor_parcelas = 0
  exced_salario = 0

  infos = [
    { "label": "Valor da Casa", "value": 0 },
    { "label": "Quantidade de Parcelas que deseja pagar", "value": 0 },
    { "label": "Salário", "value": 0 }
  ]

  for info in infos:
    while True:
      try:          
        print(f"Entre com {info["label"]}")
        info["value"] = int(input("→ "))
        break
      except ValueError:
        print("Apenas números!")
        pass

  valor_parcelas = infos[0]["value"] / infos[1]["value"]
  exced_salario = myUtils.calc_porc(infos[2]["value"], PORC_EXCED)

  print("===== Resultados =====")
  print(f"Empréstimo : {"Aceito" if not valor_parcelas > exced_salario else "Negado"}")

  print("===== Valores =====")
  print(f"| Valor de Cada Pacela       : {valor_parcelas:.2f}")
  print(f"| Salário Mensal (excedente) : {exced_salario:.2f}")

if __name__ == "__main__":
  main()
