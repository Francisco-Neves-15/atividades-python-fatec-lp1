# Escreva um programa que leia o salário de um
# funcionário e calcule o seu aumento. Caso o 
# salário atual seja superior a R$ 1.000,00 
# calcule um aumento de 10%, caso contrário, 
# calcule um aumento de 15%.

from myLibs import calc_porc

def main():
  print("\n===== Calculo de Aumento de Salario =====")

  VALOR_REQ = 1000
  PORC_AUMENTO_REQ = 10
  PORC_AUMENTO_BASE = 15
  sal_aumento = 0

  while True:
    try:          
      print("Entre com o Salário do Funcionário")
      sal = int(input("→ "))
      break
    except ValueError:
      print("Apenas números inteiros!")
      pass

  if sal > VALOR_REQ:
    sal_aumento = sal + calc_porc(sal, PORC_AUMENTO_REQ)
  else:
    sal_aumento = sal + calc_porc(sal, PORC_AUMENTO_BASE)
  
  print("=== Salários ===")
  print(f"| Antigo : {sal}")
  print(f"| Novo   : {sal_aumento}")

if __name__ == "__main__":
  main()
