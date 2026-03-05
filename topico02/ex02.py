# Crie um programa que leia um número inteiro 
# e mostre na tela se ele é par ou ímpar.

def is_even(num):
  return num % 2 == 0

def is_odd(num):
  return num % 2 != 0

def main():
  print("\n===== Par ou Impar? =====")
  num = 0

  while True:
    try:          
      print("Entre com o número para verificar")
      num = int(input("→ "))
      break
    except ValueError:
      print("Apenas números inteiros!")
      pass
  
  print(f"PAR   : {"Sim" if is_even(num) else "Não"}")
  print(f"IMPAR : {"Sim" if is_odd(num) else "Não"}")

if __name__ == "__main__":
  main()
