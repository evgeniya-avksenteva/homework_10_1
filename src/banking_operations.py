import re
import os
from collections import Counter
from src.utils import financial_transactions

list_transactions = financial_transactions(os.path.join("../data/operations.json"))


def search_transactions(file: list[dict], input_user: str) -> list[dict]:
    """Функция для поиска в списке словарей операций по заданной строке - описанию"""
    new_list = []
    for i in file:
        if "description" in i and re.findall(input_user, i["description"]):
            new_list.append(i)
    return new_list


def sort_transactions(operations: list[dict], categories: list) -> dict:
    """Функция для подсчета количества банковских операций определенного типа"""
    new = []
    for operation in operations:
        if "description" in operation and operation["description"] in categories:
            new.append(operation["description"])

    return Counter(new)


# if __name__ == "__main__":
#     categories_operations = [
#         "Перевод организации",
#         "Перевод с карты на карту",
#         "Перевод с карты на счет",
#         "Перевод со счета на счет",
#         "Открытие вклада",
#     ]
#     print(sort_transactions(list_transactions, categories_operations))
#     input_user = input("Введите слово для поиска: ")
#     print(search_transactions(list_transactions, input_user))
