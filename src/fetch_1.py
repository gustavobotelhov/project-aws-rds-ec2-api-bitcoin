from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os
from dotenv import load_dotenv

load_dotenv()

url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

parameters = {
 'symbol': 'BTC',  # Identificando o Bitcoin pelo símbolo
 'convert': 'BRL'  # Convertendo a cotação para USD
}

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': os.getenv('CMC_API_KEY')
}

session = Session()
session.headers.update(headers)

def get_current_quote():
  try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)

    if 'data' in data and "BTC" in data["data"]:
      quote_brl = data["data"]["BTC"]["quote"]["BRL"]["price"]
      last_update = data["data"]["BTC"]["quote"]["BRL"]["last_updated"]
    else: 
      print("Error retrieving bitcoin quote")

    print(f"BTC - BRL current quote: {quote_brl:.2f}")
    print(f"The last updated ocurred at {last_update}")
  except (ConnectionError, Timeout, TooManyRedirects) as e: 
    print(f"Connectcion error: {e}")

get_current_quote()
