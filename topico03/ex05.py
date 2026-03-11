# Usando for, faça um programa que leia um número 
# inteiro e mostre na tela se é ou não um número primo.

from myLibs import ask_input, is_prime

def main():
  print("\n ===== É Primo ou Não? =====")

  while True:
    num = ask_input("Digite o número para verificar", "int")
    
    if is_prime(num):
      print("É Primo!")
    else:
      print("Não é Primo!")

if __name__ == "__main__":
  main()
