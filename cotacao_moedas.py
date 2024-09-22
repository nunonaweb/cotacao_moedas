# 
# power by brunoborges.eti.br
# 
import requests
import matplotlib.pyplot as plt
from datetime import datetime
def get_currency_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        dates = [datetime.fromtimestamp(int(item['timestamp'])).strftime('%Y-%m-%d') for item in data]
        rates = [float(item['high']) for item in data]
        return dates, rates
    else:
        print(f"Erro ao buscar dados da API {url}: {response.status_code}")
        return [], []
# URLs das APIs
url_dolar = "https://economia.awesomeapi.com.br/json/daily/USD-BRL/15"
url_euro = "https://economia.awesomeapi.com.br/json/daily/EUR-BRL/15"
url_libra = "https://economia.awesomeapi.com.br/json/daily/GBP-BRL/15"

# Obter os dados de cada moeda:
dates_dolar, rates_dolar = get_currency_data(url_dolar)
dates_euro, rates_euro = get_currency_data(url_euro)
dates_libra, rates_libra = get_currency_data(url_libra)
# Verificar se todos os dados foram obtidos com sucesso
if not dates_dolar or not rates_dolar or not dates_euro or not rates_euro or not dates_libra or not rates_libra:
    print("Erro ao obter todos os dados. Verifique as URLs das APIs e sua conexão com a internet.")
    exit()
# Criar o gráfico
plt.figure(figsize=(20, 6))
plt.plot(dates_dolar, rates_dolar, label='Dólar', marker='o')
plt.plot(dates_euro, rates_euro, label='Euro', marker='s')
plt.plot(dates_libra, rates_libra, label='Libra', marker='^')
plt.xlabel('Data')
plt.ylabel('Cotação (BRL)')
plt.title('Cotação de Moedas (USD-BRL, EUR-BRL, GBP-BRL) - Últimos 15 Dias')
plt.grid(True)
plt.legend()
plt.xticks(rotation=45)
plt.savefig('cotacoes_moedas.png', dpi=300)
print("Gráfico salvo com sucesso como cotacoes_moedas.png")