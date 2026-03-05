# Implemente um programa que leia um número inteiro e mostre seu sucessor e seu antecessor.

def ex01():
  print("\n ===== Anterior & Sucessor do Número =====")

  print("Digite um número inteiro: ")
  while True:
    try:
      num = int(input("→ "))
      break
    except ValueError:
      print("ERROR: Digite apenas números!")
      pass
  
  print(f"""
Anterior : {num - 1} 
Número   : {num} 
Sucessor : {num + 1} 
  """)

if __name__ == "__main__":
  ex01()