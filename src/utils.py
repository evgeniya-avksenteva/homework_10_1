import json
from typing import Any
from src.external_api import currency_conversion


def financial_transactions(path: str) -> Any:
    """Функция принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, encoding="utf-8") as financial_file:
            try:
                transactions = json.load(financial_file)
            except json.JSONDecodeError:  # Ошибка декорирования файла
                return []
        if not isinstance(transactions, list):  # Файл содержит не список
            return []
        return transactions
    except FileNotFoundError:  # Файл не найден
        return []


# print(financial_transactions('../data/operations.json'))


def transaction_amount(trans: dict, currency: str = "RUB") -> Any:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    if trans["operationAmount"]["currency"]["code"] == currency:
        amount = trans["operationAmount"]["amount"]
    else:
        amount = currency_conversion(trans)
    return amount


# print(transaction_amount())
