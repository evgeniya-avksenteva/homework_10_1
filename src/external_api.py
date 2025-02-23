import os
from dotenv import load_dotenv
import requests


load_dotenv()

API_KEY = os.getenv("API_KEY")


def currency_conversion(transaction: dict) -> float:
    """ Функция конвертации """
    headers = {"apikey": API_KEY}
    amout = transaction["operationAmount"]["amount"]
    code = transaction["operationAmount"]["currency"]["code"]
    to = "RUB"
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={code}&amount={amout}"
    payload = {}
    response = requests.get(url, headers=headers, data=payload)
    result = response.json()
    return round(result["result"], 2)


# print(currency_conversion())
