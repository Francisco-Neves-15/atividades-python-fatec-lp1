# Faça um programa para jogar Jokenpô (clássico pedra, papel 
# e tesoura) com você. Você deverá informar uma das opções, 
# o programa deverá então sortear uma das três opções possíveis
# e mostrar quem ganhou na tela.

# Código Relizado a tempos;
# Verifique em: https://onecompiler.com/python/442r7y8jq
# Adaptado para jogar contra a máquina

import random
import time

REGRAS = {
  "MAOS": [
    "TESOURA",
    "PAPEL",
    "PEDRA",
    "PISTOLA",
    "ESCUDO",
    "AMIZADE",
    "FOGO",
    "AGUA",
    "VENTO"
  ],
  "TESOURA": ["PAPEL", "AMIZADE", "VENTO"],
  "PAPEL": ["PEDRA", "ESCUDO", "FOGO"],
  "PEDRA": ["TESOURA", "PISTOLA", "VENTO"],
  "PISTOLA": ["TESOURA", "PAPEL", "AMIZADE"],
  "ESCUDO": ["PISTOLA", "TESOURA", "FOGO"],
  "AMIZADE": ["PISTOLA", "PEDRA", "ESCUDO"],
  "FOGO": ["PAPEL", "AMIZADE", "VENTO"],
  "AGUA": ["FOGO", "PISTOLA", "PEDRA"],
  "VENTO": ["FOGO", "AGUA", "PAPEL"]
}

def jogar(player1, player2, rodadas):
  print(f"\n=== Rodada {rodadas} | {player1} vs {player2} ===")

  if player1 == player2:
    print(f"Empate! — {player1} empata com {player2}")
  elif player2 in REGRAS[player1]:
    print(f"Ganhou! — {player1} ganha de {player2}")
  elif player1 in REGRAS[player2]:
    print(f"Perdeu! — {player1} perde de {player2}")
  else:
    print(f"Sem resultado definido entre {player1} e {player2}")

  print("\n")

def main():
  rodadas = 0

  print("\n--- MODO INTERATIVO ---")

  print(20 * "=")
  print("Jogador 1 : Usuário")
  print("Jogador 2 : Máquina")
  print(20 * "=")

  while True:
    print(f"Opções válidas : {', '.join(REGRAS['MAOS'])}")
    print('Digite         : SAIR para encerrar')

    rodadas += 1
    print(f"\nRodada {rodadas}")

    while True:
      player1 = input("\nJogador 1: ").strip().upper()
      # player2 = input("Jogador 2: ").strip().upper()

      if player1 == "SAIR":
        print("Encerrando...")
        break

      if player1 not in REGRAS:
        print("\n!!! Jogada inválida! Tente novamente.")
      else:
        break

    # Máquina escolhe
    print("\nMáquina pensando...")
    time.sleep(1.5)
    player2 = random.choice(REGRAS["MAOS"])
    print(f"\nMáquina: {player2}")
    jogar(player1, player2, rodadas)

if __name__ == "__main__":
  main()
