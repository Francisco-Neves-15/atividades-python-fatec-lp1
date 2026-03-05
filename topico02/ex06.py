# Faça um program que leia o ano de nascimento de uma
# pessoa e informe se ele ainda vai se alistar ao serviço 
# militar ou se ele está no período de se alistar ou se 
# ele perdeu o prazo para se alistar. Além disso, mostre 
# também a quantidade de anos que falta para se alistar 
# ou que passou do prazo.

from myUtils import myUtils
from datetime import date

def main():
  print("\n===== Cálculo do Alistamento =====")

  ANO_ATUAL = date.today().year
  IDADE_MAXIMA_ALISTAMENTO = 18

  ano_nascimento = 0
  ano_alistar = 0

  perdeu_prazo = False
  anos_prazo = False

  ano_nascimento = myUtils.ask_input("Entre o ANO do Nascimento", "int")
  ano_alistar = ano_nascimento + IDADE_MAXIMA_ALISTAMENTO

  perdeu_prazo = True if ANO_ATUAL > ano_alistar else False

  if perdeu_prazo:
    anos_prazo = ANO_ATUAL - ano_alistar
  else:
    anos_prazo = ano_alistar - ANO_ATUAL

  print("===== Resultados =====")
  print(f"| Ano Nascimento    : {ano_nascimento}")
  print(f"| Ano de se Alistar : {ano_alistar}")
  print(f"| Perdeu o Prazo    : {"Sim" if perdeu_prazo else "Não"}")
  print(f"| {f"Anos Perdidos" if perdeu_prazo else "Anos Restantes"}: {anos_prazo}")

if __name__ == "__main__":
  main()
