# Peça para o usuário digitar o seu ano de nascimento. O programa deve calcular
# e mostrar a idade atual dele, considerando que o ano atual é 2026.

from datetime import datetime
from calendar import monthrange

def diferenca_completa(data_inicio, data_final):

    anos = data_final.year - data_inicio.year
    meses = data_final.month - data_inicio.month
    dias = data_final.day - data_inicio.day

    if dias < 0:
        meses -= 1
        dias_no_mes = monthrange(data_final.year, (data_final.month-1) or 12)[1]
        dias += dias_no_mes

    if meses < 0:
        anos -= 1
        meses += 12

    return anos, meses, dias

def ex06():
  print("\n ===== Comparadora de Datas =====")

  infos = [
    { "label": "Ano", "value": 0 },
    { "label": "Mês", "value": 0 },
    { "label": "Dia", "value": 0 },
    { "label": "Hora", "value": 0 },
    { "label": "Minuto", "value": 0 },
  ]

  data_inicio = ""
  data_final = ""
  diff = ""

  for info in infos:
  
    while True:
      print(f'Entre com o {info["label"]} (caso não queira, digite "skip" ): ')
      num = input("→ ")

      if num.upper() == "SKIP":
        break

      try:
        num = int(num)
      except ValueError: 
        print("ERROR: Digite apenas números!")
        pass
        
      else:
        info["value"] = num
        break

  print(infos)

  data_inicio = datetime(infos[0]["value"], infos[1]["value"], infos[2]["value"], infos[3]["value"], infos[4]["value"])
  data_final = datetime.now()
  diff = data_final - data_inicio

  anos, meses, dias = diferenca_completa(data_inicio, data_final)
  print(f"Diferença Completa: {diff}")
  print(f"{anos} anos, {meses} meses, {dias} dias")

if __name__ == "__main__":
  ex06()
