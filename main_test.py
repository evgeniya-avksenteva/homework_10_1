import os
import re
import pandas as pd

from src.masks import get_mask_account, get_mask_card_number
from src.utils import financial_transactions, transaction_amount
from src.generators import filter_by_currency
from src.transactions_file import read_transaction_csv, read_transaction_excel
from src.banking_operations import sort_transactions, search_transactions
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card


def main() -> str:
    greeting = """Привет! Добро пожаловать в программу работы
с банковскими транзакциями.
Выберите необходимый пункт меню:\n
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""
    input_user_file = input(f"{greeting}\n")

    while input_user_file not in ["1", "2", "3"]:
        print("\nВведен некорректный ответ\nПопробуйте еще раз:")
        input_user_file = input()

    else:

        if input_user_file == "1":
            print("\nДля обработки выбран JSON-файл.")
            path_to_file = os.path.join(os.path.dirname(__file__), "data", "operations.json")
            result = financial_transactions(path_to_file)

        elif input_user_file == "2":
            print("\nДля обработки выбран CSV-файл.")
            path = os.path.join(os.path.dirname(__file__), "data", "transactions.csv")
            result = read_transaction_csv(path)

        elif input_user_file == "3":
            print("\nДля обработки выбран XLSX-файл.")
            path = os.path.join(os.path.dirname(__file__), "data", "transactions_excel.xlsx")
            result = read_transaction_excel(path)





if __name__ == "__main__":
    main()