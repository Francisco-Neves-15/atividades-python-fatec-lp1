# Implemente o jogo da forca. Um usuário deverá entrar 
# com uma palavra. Em seguida, outro usuário deverá 
# indicar as letras dessa palavra. Caso exista, deverá 
# ser mostrada as letras e as suas posições na palavra. 
# Caso não exista, o usuário perderá uma chance. No total, 
# o usuário terá 6 chances para acertar.

# Luiz Francisco Neves Mendes

# Uma versão deste código já existia devido aos exercícios
# extras do tópico 3, ele apenas foi aprimorado.

from getpass import getpass

# ==================================================

def mostrar_win():
  print("=" * 20)
  print("Você ganhou!")
  print("=" * 20)

def mostrar_progresso(lista):
  print(" ".join(lista))

def mostrar_vidas(vidas):
  print("Vidas:", "♥ " * vidas)

def main():
  print("\n ===== Jogo da Forca =====")

  LIMITE_VIDAS = 6

  print(f"Entre com a palavra (não aparece ao digitar)")
  PALAVRA_ACERTO = getpass("→ ").upper()

  progresso = ["_"] * len(PALAVRA_ACERTO)
  letras_tentadas = []

  win = False
  tentativas = 0
  vidas = LIMITE_VIDAS

  while not win and vidas > 0:
    tentativas += 1

    print(f"\n{tentativas}° tentativa")
    mostrar_vidas(vidas)
    mostrar_progresso(progresso)

    print("=" * 20 + "\n")
    print(f"Letras tentadas: {', '.join(letras_tentadas) if letras_tentadas else '-'}")
    print("| UMA letra para tentativa")
    print("| OU  a palavra")

    user_entry = input("→ ").upper()

    if user_entry in letras_tentadas:
      print("\n ! Você já tentou essa letra!")
      continue

    if len(user_entry) > 1:

      if user_entry == PALAVRA_ACERTO:
        mostrar_win()
        progresso = list(PALAVRA_ACERTO)
        mostrar_progresso(progresso)
        win = True
      else:
        print("Errou a palavra!")
        vidas -= 1
    
    else:

      letras_tentadas.append(user_entry)

      encontrado = False

      for index, letra in enumerate(PALAVRA_ACERTO):
        if user_entry == letra:
          progresso[index] = letra
          encontrado = True

      if encontrado:
        print(f"Letra: {user_entry} está na palavra!")
      else:
        print(f"Letra: {user_entry} NÃO está na palavra!")
        vidas -= 1

      mostrar_progresso(progresso)

      print("=" * 20 + "\n")

      if "_" not in progresso:
        mostrar_win()
        win = True

  if not win:
    print("\nFim de jogo! Você perdeu.")
    print(f"Palavra era: *segredo*")

# ==================================================

if __name__ == "__main__":
  main()
