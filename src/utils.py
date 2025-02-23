import json
import os.path
from typing import Any

from src.external_api import currency_conversion


def financial_transactions(path: str) -> Any:
    """Функция принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях"""
    if not os.path.exists(path):
        return []

    try:
        with open(path, "r", encoding="utf-8") as financial_file:
            try:
                transactions = json.load(financial_file)
            except json.JSONDecodeError:  # Ошибка декорирования файла
                return []
        if not isinstance(transactions, list):  # Файл содержит не список
            return []
        return transactions
    except FileNotFoundError:  # Файл не найден
        return []


path_file_test_1 = "../data/test_1.json"
path_file_test_2 = "../data/test_2.json"
path_file_operations = "../data/operations.json"

if __name__ == "__main__":
    print(financial_transactions(path_file_operations))


def transaction_amount(trans: dict, currency: str = "RUB") -> Any:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    if trans["operationAmount"]["currency"]["code"] == currency:
        amount = trans["operationAmount"]["amount"]
    else:
        amount = currency_conversion(trans)
    return amount


# if __name__ == '__main__':
# print(transaction_amount())
