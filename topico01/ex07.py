# Implemente um programa que tenha como entrada o valor em
# reais e mostre o valor correspondente em dólar.

import requests

def get_exchange_rate(currency_code, base_currency="BRL"):
    url = f"https://economia.awesomeapi.com.br/json/last/{currency_code}-{base_currency}"
    
    try:
        print("Aguardando resposta...")
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        key = f"{currency_code}{base_currency}"
        code = data[key]['code']
        codein = data[key]['codein']
        bid = data[key]['bid']
        create_date = data[key]['create_date']
        
        return code, codein, bid, create_date

    except requests.RequestException as e:
        print(f"Falha ao buscar: {e}")
        return None, None, None, None

def ex07():
    print("\n ===== Comparadora de Cotação entre Moedas =====")
    
    print("Entre com a Moeda que deseja consultar (ex: USD, EUR): ")
    currency_code = input("→ ").upper()
    print("Entre com a Moeda base (padrão BRL): ")
    base_currency = input("→ ").upper() or "BRL"
    
    code, codein, bid, create_date = get_exchange_rate(currency_code, base_currency)

    if code:
        print(f"""
| Moeda cotada   : {code}
| Moeda base     : {codein}
| Cotação        : {bid}
| Busca feita em : {create_date}
""")
    else:
        print("Não foi possível obter a cotação.")

if __name__ == "__main__":
    ex07()