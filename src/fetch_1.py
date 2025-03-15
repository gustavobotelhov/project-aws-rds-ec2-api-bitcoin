from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os
from dotenv import load_dotenv

load_dotenv()

url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

parameters = {
 'symbol': 'BTC',  # Identificando o Bitcoin pelo símbolo
 'convert': 'USD'  # Convertendo a cotação para USD
}

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': os.getenv('CMC_API_KEY')
}

session = Session()
session.headers.update(headers)

response = session.get(url, params=parameters)

data = response.json()

print(data)

