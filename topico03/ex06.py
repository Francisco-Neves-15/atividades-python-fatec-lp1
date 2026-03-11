# Você recebe uma string e sua tarefa é trocar casos. 
# Em outras palavras, converta todas as letras minúsculas
# em maiúsculas e vice-versa.
# Input: Fatec Rio Preto
# Output: fATEC rIO pRETO

from myLibs import ask_input

def main():
  print("\n ===== Inversor de Case das Palavras =====")

  word = ask_input("Digite o número para verificar", "string")
  new_word = ""
  
  for letra in word:

    if letra in [" ", " "]:
      new_word += letra
      continue

    if letra.isupper():
      letra = letra.lower()
    else:
      letra = letra.upper()

    new_word += letra
  
  print(f"Palavra      : {word}")
  print(f"Nova palavra : {new_word}")

if __name__ == "__main__":
  main()
