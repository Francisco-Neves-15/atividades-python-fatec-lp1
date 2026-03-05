# Escreva um programa que leia a velocidade de um carro. 
# Se esta velocidade for maior que 80Km/h o programa deverá
# escrever uma mensagem na tela avisando que o usuário levou
# uma multa e o valor a ser pago. Considere R$ 7 reais por
# cada Km acima do limite.

def main():
  print("\n===== Sistema de Multa por Velocidade =====")

  LIMITE_VELOCIDADE_KM = 80
  VALOR_POR_KM_ACIMA = 7

  velocidade_detectada = 0
  km_acima = 0
  multa = 0

  while True:
    try:          
      print("Velocidade Detectada (Km/h): ")
      velocidade_detectada = float(input("→ "))
      break
    except ValueError:
      print("Apenas números!")
      pass
  
  if velocidade_detectada > LIMITE_VELOCIDADE_KM:
    km_acima = velocidade_detectada - LIMITE_VELOCIDADE_KM
    multa = km_acima * VALOR_POR_KM_ACIMA

  print("===== Tabela =====")
  print(f"Velocidade : {velocidade_detectada}")
  print("Nada Anormal" if multa <= 0 else f"Limite Anormal! \nValor da Multa: {multa}")

if __name__ == "__main__":
  main()
