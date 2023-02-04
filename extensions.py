import json
import requests
from config import keys
from config import TOKEN

class APIException(Exception):
     pass

class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

     if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')
    def convert(quote: str, base: str, amount: str):
        # if quote == base:
        #     raise APIException(f'Невозможно перевести одинаковые валюты {base}. ')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')
            raise APIException(f'Не удалось обработать валюту {quote}. ')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')
            raise APIException(f'Не удалось обработать валюту {base}. ')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество{amount}')
            raise APIException(f'Не удалось обработать количество {amount}. ')

        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}. ')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]
        total_base = json.loads(r.content)[keys[base]] * float(amount)

        return total_base

        return total_base