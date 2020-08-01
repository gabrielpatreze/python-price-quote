#procurar api
import requests
import json
import time
import datetime
#biblioteca time e datetime para ver tempo real


while True:
#loop infinito

    requisicao = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL,EUR-BRL,BTC-BRL')

    cotacao = json.loads(requisicao.text)

    print('>>> Cotação Dólar, Euro, Bitcoin <<< Data e hora:', datetime.datetime.now())
    print('')
    print('Alta do dólar: $', cotacao['USD']['high'])
    print('Baixa do dólar: $', cotacao['USD']['low'])
    print('')
    print('Alta do euro: $', cotacao['EUR']['high'])
    print('Baixa do euro: $', cotacao['EUR']['low'])
    print('')
    print('Alta do bitcoin: $', cotacao['BTC']['high'])
    print('Baixa do bitcoin: $', cotacao['BTC']['low'])
    time.sleep(3)
    #espera 3 segundos para ver cotação novamente