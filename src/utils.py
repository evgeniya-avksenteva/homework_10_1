import json
import logging
from typing import Any

from src.external_api import currency_conversion

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("utils_log.log", "w")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def financial_transactions(path: str) -> Any:
    """Функция принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        logger.info("Открываю файл с транзакциями")
        with open(path, "r", encoding="utf-8") as financial_file:
            transactions = json.load(financial_file)
            if not isinstance(transactions, list):  # Файл содержит не список
                logger.error("Список транзакций пуст")
                return []
            logger.info("Сформирован список с данными о финансовых транзакциях")
            return transactions
    except json.JSONDecodeError:  # Ошибка декорирования файла
        logger.error("Ошибка декорирования файла")
        return []
    except FileNotFoundError:  # Файл не найден
        logger.error("Файл с транзакциями не найден")
        return []


path_file_test_1 = "../data/test_1.json"
path_file_test_2 = "../data/test_2.json"
path_file_operations = "../data/operations.json"

# if __name__ == "__main__":
#    print(financial_transactions(path_file_operations))


def transaction_amount(transaction: dict, currency: str = "RUB") -> Any:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    if transaction["operationAmount"]["currency"]["code"] == currency:
        amount = transaction["operationAmount"]["amount"]
        logger.info("Код валюты в транзакции RUB")
    else:
        amount = currency_conversion(transaction)
        logger.info("Иной код валюты транзакции, произведена конвертация")
    return amount


#if __name__ == '__main__':
#    print(transaction_amount())
