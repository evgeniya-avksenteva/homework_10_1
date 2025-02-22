import json
import os
from json import JSONDecodeError
from typing import Any

# from src.external_api import currency_conversion


def financial_transactions(path: str) -> Any:
    """ Функция принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях """
    try:
        with open(path, encoding="utf-8") as financial_file:
            try:
                transactions = json.load(financial_file)
            except json.JSONDecodeError:
                print("Ошибка декорирования файла")
                return []
        if not isinstance(transactions, list):
                print("Файл содержит не список")
                return []
        return transactions
    except FileNotFoundError:
        print("Файл не найден")
        return []

# print(financial_transactions('../data/operations.json'))

