#

import random
import json

from myLibs import ask_input

with open("topico03/some-word-list.json", "r", encoding="utf-8") as f:
  PALAVRAS = json.load(f)

VERSIONS = ["v1", "v2"]

# ====================================================================================================

def v1():
  print("\n ===== Jogo da Forca Básico (v1) =====")

  correct_word = random.choice(PALAVRAS).upper()

  win = False
  tentativas = 0
  while not win:
    tentativas += 1

    print("")
    user_entry = ask_input(f"{tentativas}° tentativa \n| UMA letra para tentativa \n| OU a palavra \n| 1 -{correct_word}-\n",  "string").upper()

    if len(user_entry) > 1:

      if user_entry == correct_word:
        print("Você ganhou!")
        win = True
      else:
        print("Errou!")
        break
    
    else:

      encontrado = False
      for index, letra in enumerate(correct_word, start=1):

        if index == 1:
          print(len(correct_word))

        if user_entry == letra:
          print(f"Letra: {user_entry} está na palavra, na {index}° posição.")
          encontrado = True

      if not encontrado and index == len(correct_word):
        print(f"Letra: {user_entry} -> NÃO está na palavra!")

# ====================================================================================================

def v2():
  print("\n ===== Jogo da Forca Básico (v2 in dev) =====")

def main():
  print("==== Qual versão será jogada? ====")
  v = ask_input("Email a ser validado", "string")
  if v in VERSIONS:
    match v:
      case "v1":
        v1()
      case "v2":
        v2()
  else:
    print("Versão Inexistent!")

if __name__ == "__main__":
  # main()
  v1()
