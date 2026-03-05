# Implemente um programa que leia 4 notas de um aluno
# e mostre a média aritmética.

def ex02():
  print("\n ===== Leitor de N notas & Média dessas =====")

  print('Digite as notas abaixo (ou "fim" para encerrar)')

  notas = []
  total = 0
  media = 0

  while True:
    num = input("→ ")

    if num.upper() == "FIM":
      break

    try:
      num = float(num)
    except ValueError: 
      print("ERROR: Digite apenas números!")
      pass
      
    else:
      notas.append(num)
  
  for index, nota in enumerate(notas, start=1):
    total += nota
    print(f"| {index}° nota: {nota}")

  media = total / len(notas)
  print(f"|   Média: {media}")

if __name__ == "__main__":
  ex02()
