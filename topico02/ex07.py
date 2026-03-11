# Crie um programa que, dada a altura e peso de uma pessoa, 
# calcule o seu IMC (Índice de Massa Corporal) e indique sua 
# situação de acordo com a tabela abaixo. O cálculo do IMC é
# feito pela divisão do peso pela altura ao quadrado.
#  Abaixo de 17. Muito abaixo do peso
#  Entre 17 e 18,49 Abaixo do peso
#  Entre 18,5 e 24,99 Peso normal
#  Entre 25 e 29,99 Acima do peso
#  Entre 30 e 34,99 Obesidade I
#  Entre 35 e 39,99 Obesidade II (severa)
#  Acima de 40 Obesidade III (mórbida)

from myLibs import ask_input

tabela = [
  { "min": 0,    "max": 16.99, "nivel": "Muito abaixo do peso" },
  { "min": 17,   "max": 18.49, "nivel": "Abaixo do peso" },
  { "min": 18.5, "max": 24.99, "nivel": "Peso normal" },
  { "min": 25,   "max": 29.99, "nivel": "Acima do peso" },
  { "min": 30,   "max": 34.99, "nivel": "Obesidade I" },
  { "min": 35,   "max": 39.99, "nivel": "Obesidade II (severa)" },
  { "min": 40,   "max": float("inf"), "nivel": "Obesidade III (mórbida)" }
]

def main():
  print("\n===== Cálculo de IMC =====")

  imc_valor = 0
  resultado = 0

  altura_cm = ask_input("Altura (cm)", "int")
  peso_k = ask_input("Peso (K)", "int")

  imc_valor = round(( peso_k / ( altura_cm * 2 ) ) * 100, 2)

  for index, item in enumerate(tabela):
    if imc_valor >= item["min"] and imc_valor <= item["max"]:
      resultado = tabela[index]
      break
    else:
      pass

  print("===== Resultados =====")
  print(f"| IMC   : {imc_valor}")
  print(f"| Nível : {resultado["nivel"]}")

if __name__ == "__main__":
  main()
