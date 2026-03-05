# Escreva um programa que leia a temperatura em Celsius e converta para Fahrenheit. A fórmula de conversão é:
# 𝐹  = 𝐶 × 9/5 + 32

def ex05():
  
  def Fahrenheit(celsius):
    return celsius * ( 9/5 ) + 32
  
  print("\n ===== Celsius para Fahrenheit =====")

  print("Digite a temperatura: ")
  while True:
    try:
      num = int(input("→ "))
      break
    except ValueError:
      print("ERROR: Digite apenas números!")
      pass

  print(f"Celsius    : {num}")
  print(f"Fahrenheit : {Fahrenheit(num)}")

if __name__ == "__main__":
  ex05()
