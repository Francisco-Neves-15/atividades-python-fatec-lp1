# Faça um programa que faça a entrada de um texto. 
# Se for um e-mail, retorne "E-mail válido", caso contrário,
# retorne "E-mail inválido". Para tanto, verifique se o texto
# possui o símbolo @

from myLibs import ask_input

def main():
  print("\n ===== Validador de Email =====")

  word = ask_input("Email a ser validado", "string")
  
  for letra in word:
    if letra == "@":
      print('Valido!')
      break
  else:
    print("Não Valido!")

if __name__ == "__main__":
  main()
