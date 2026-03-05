# Faça um programa em que ele sorteie um número entre 0 e 5. 
# O usuário deverá então adivinhar este número e o programa
# deverá escrever na tela se ele acertou ou não.

import random

def say_more_or_less(chute_usuario, num_sorteado):
  if num_sorteado > chute_usuario:
    print(";) | Tente mais alto!")
    return False
  elif num_sorteado < chute_usuario:
    print(";) | Tente mais baixo!")
    return False

def check_value(chute_usuario, num_sorteado):
  print(chute_usuario, num_sorteado)
  if chute_usuario > num_sorteado:
    return False
  elif chute_usuario < num_sorteado:
    return False
  else:
    return True


def main():
  print("\n===== Adivinhe o número! =====")

  NUM_RANGE = 5
  NUM_RANGE_LIST = [i for i in range(NUM_RANGE)]
  chute_usuario = 0
  num_sorteado = 0
  tentativas = 0

  num_sorteado = random.choice(NUM_RANGE_LIST)

  print(":) | SiMiSi diz: Tente adivinhar o número que estou pensando ?", num_sorteado)

  while True:
    try:          
      chute_usuario = int(input("→ "))
      break
    except ValueError:
      print(">:( | SiMiSi diz: Apenas números!")
      pass

  tentativas += 1

  if check_value(chute_usuario, num_sorteado):
    print(":o | Acertou!")
    print(f":D | SiMiSi diz: Tentativas: {tentativas}")

  else:
    while True:
      say_more_or_less(chute_usuario, num_sorteado )
      print(';) | SiMiSi diz: Tentar novamente? Apenas chute ou digite: "n"')

      tentar = input("→ ")

      if tentar.upper() in ["N", "NÃO", "NAO", "NO"]:
        print(";( | SiMiSi diz: Que pena!")
        print(f":o | SiMiSi diz: Tentativas: {tentativas}")
        print(f":) | SiMiSi diz: O Número era: *segredo*")
        break
      else:
        try:
          tentar = int(tentar)
          tentativas += 1
        except ValueError:
          print(">:( | SiMiSi diz: Apenas números!")
          pass

        if check_value(tentar, num_sorteado):
          print(":o | Acertou!")
          print(f":D | SiMiSi diz: Tentativas: {tentativas}")
          break

if __name__ == "__main__":
  main()
