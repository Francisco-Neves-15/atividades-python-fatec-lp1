# Usando while, escreva um programa que cadastre o estado civil 
# de uma pessoa, entretanto, o programa deve continuar
# perguntando enquanto o valor informado for diferente 
# de "solteiro" ou "casado".

from myLibs import ask_input

def ex01():
  print("\n ===== Cadastro de Pessoas =====")

  pessoas = []
  estados_civis_possiveis = ["solteiro", "casado"]

  index = 1
  while True:
    nova_pessoa = {"nome": "", "estado_civil": ""}

    nova_pessoa["nome"] = ask_input(f'Nome da {index}° pessoa | ou "fim" para encerrar', "string")

    if nova_pessoa["nome"] == "fim":
      break

    nova_pessoa["estado_civil"] = ask_input(f'Estado Civil entre "{", ".join(estados_civis_possiveis)}"', "string").lower()
  
    if nova_pessoa["estado_civil"] not in estados_civis_possiveis:
      print("Esse estado civil não está nas opções! Digite novamente.")
      continue
    else:
      pessoas.append(nova_pessoa)
    
    index += 1

  for index, pessoa in enumerate(pessoas, start=1):
    print(f'{index}° | {pessoa["nome"]} | {pessoa["estado_civil"]}')

if __name__ == "__main__":
  ex01()
