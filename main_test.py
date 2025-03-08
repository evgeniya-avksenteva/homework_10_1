import os
import re
import pandas as pd
import csv

from src.utils import financial_transactions
from src.generators import filter_by_currency
from src.transactions_file import read_transaction_csv, read_transaction_excel
from src.banking_operations import sort_transactions, search_transactions
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card
from tests.test_generators import transactions_1


def main() -> None:
    """Функция, которая отвечает за основную логику проекта и связывает функции между собой."""
    while True:
        print(
            """Привет! Добро пожаловать в программу работы с банковскими транзакциями.
        Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла"""
        )
        user_file_choice = input().strip()
        if user_file_choice == "1":
            print("Выбран JSON-файл.")
            transactions_list = financial_transactions(
                os.path.join(os.path.dirname(__file__), "data", "operations.json"))
            break
        elif user_file_choice == "2":
            print("Выбран CSV-файл.")
            transactions_list = read_transaction_csv(
                os.path.join(os.path.dirname(__file__), "data", "transactions.csv"))
            break
        elif user_file_choice == "3":
            print("Выбран XLSX-файл.")
            transactions_list = os.path.join(os.path.dirname(__file__), "data", "transactions_excel.xlsx")
            break
        else:
            print("Некорректный выбор. Попробуй еще раз.")
            continue

    transactions_list: dict[str, str | bool] = {}
    while True:
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию. "
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING:\n"
        ).upper()
        if status in ["CANCELED", "PENDING", "EXECUTED"]:
            # filters - transactions ["status"] = status
            transactions_list = filter_by_state(transactions_list, status)
            print(f"Операции отфильтрованы по статусу {status}")
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")

    while True:
        sort_date = input("Отсортировать операции по дате? Да/Нет\n").lower()
        if sort_date == "да":
            while True:
                sorting_order = input(
                    """Отсортировать по возрастанию или по убыванию? по возрастанию/по убыванию\n"""
                ).lower()
                if sorting_order == "по возрастанию":
                    # filters["date"] = False
                    transactions_list = sort_by_date(data_list, sort: bool = False)
                    break
                elif sorting_order == "по убыванию":
                    transactions_list = sort_by_date(data_list, sort: bool = True)
                    # filters["date"] = True
                    break
                else:
                    print("Некорректный выбор. Попробуйте еще раз.")
                    continue
            break
        elif sort_date == "нет":
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")
            continue

        #while True:
        sort_code = str(input("Выводить только рублевые транзакции? Да/Нет\n")).lower()
        if sort_code == "да":
            filters["currency"] = "RUB"
            break
        elif sort_code == "нет":
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")
            continue
    while True:
        user_input = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет:\n").lower()
        if user_input == "да":
            search = input("Видите слово для поиска: ")
            filters["description"] = search
            break
        elif user_input == "нет":
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")
            continue

    transactions = transactions_list
    for filter_type, filter_value in filters.items():
        if filter_type == "status":
            transactions = filter_by_state(transactions, filter_value)
        elif filter_type == "date":
            transactions = sort_by_date(transactions, filter_value)
        elif filter_type == "currency":
            transactions = [
                tr
                for tr in transactions
                if tr.get("operationAmount", {}).get("currency", {}).get("code") == filter_value
            ]
        elif filter_type == "description":
            transactions = search_transactions(transactions, filter_value)

    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(transactions)}")

    for transaction in transactions:
        description = transaction.get("description")
        if description == "Открытие вклада":
            from_ = description
        else:
            from_ = mask_account_card(transaction.get("from"))

        to_ = mask_account_card(transaction.get("to"))
        date = get_date(transaction.get("date"))

        amount = transaction["operationAmount"]["amount"]
        currency = transaction["operationAmount"]["currency"]["name"]

        if description == "Открытие вклада":
            print(f"{date} {description}\nСчет {to_}\nСумма: {amount} {currency}\n")
        else:
            print(f"{date} {description}\n{from_} -> {to_}\nСумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()



    for filter_type, filter_value in transactions_list.items():
        if filter_type == "status":
            transactions = filter_by_state(transactions, filter_value)
        elif filter_type == "date":
            transactions = sort_by_date(transactions, filter_value)
        elif filter_type == "currency":
            transactions = [
                tr
                for tr in transactions
                if tr.get("operationAmount", {}).get("currency", {}).get("code") == filter_value
            ]
        elif filter_type == "description":
            transactions = search_transactions(transactions, filter_value)

    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(transactions)}")

    for transaction in transactions:
        description = transaction.get("description")
        if description == "Открытие вклада":
            from_ = description
        else:
            from_ = mask_account_card(transaction.get("from"))

        to_ = mask_account_card(transaction.get("to"))
        date = get_date(transaction.get("date"))

        amount = transaction["operationAmount"]["amount"]
        currency = transaction["operationAmount"]["currency"]["name"]

        if description == "Открытие вклада":
            print(f"{date} {description}\nСчет {to_}\nСумма: {amount} {currency}\n")
        else:
            print(f"{date} {description}\n{from_} -> {to_}\nСумма: {amount} {currency}\n")







#    for filter_type, filter_value in transactions_list.items():
#       if filter_type == "status":
#            transactions = filter_by_state(transactions, filter_value)
#        elif filter_type == "date":
#            transactions = sort_by_date(transactions, filter_value)
#        elif filter_type == "currency":
#            transactions = [
#                tr
#                for tr in transactions
#                if tr.get("operationAmount", {}).get("currency", {}).get("code") == filter_value
#            ]
#        elif filter_type == "description":
#            transactions = search_transactions(transactions, filter_value)
#
#    print("Распечатываю итоговый список транзакций...")
#
#    if not transactions_list:
#        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
#        return
#    else:
#    # print("Распечатываю итоговый список транзакций...")
#        print(f"Всего банковских операций в выборке: {len(transactions_list)}")

#    for transaction in transactions_list:
#        description = transaction.get("description")
#        if description == "Открытие вклада":
#            from_ = description
#        else:
#            from_ = mask_account_card(transaction.get("from"))
#
#        to_ = mask_account_card(transaction.get("to"))
#        date = get_date(transaction.get("date"))
#
#        amount = transaction["operationAmount"]["amount"]
#        currency = transaction["operationAmount"]["currency"]["name"]
#
#        if description == "Открытие вклада":
#            print(f"{date} {description}\nСчет {to_}\nСумма: {amount} {currency}\n")
#        else:
#            print(f"{date} {description}\n{from_} -> {to_}\nСумма: {amount} {currency}\n")

    for filter_type, filter_value in transactions_list.items():
        if filter_type == "status":
            transactions = filter_by_state(transactions, filter_value)
        elif filter_type == "date":
            transactions = sort_by_date(transactions, filter_value)
        elif filter_type == "currency":
            transactions = [
                tr
                for tr in transactions
                if tr.get("operationAmount", {}).get("currency", {}).get("code") == filter_value
            ]
        elif filter_type == "description":
            transactions = search_transactions(transactions, filter_value)

    print("Распечатываю итоговый список транзакций...")

    if not transactions_list:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return
    else:
    # print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(transactions_list)}")

    for transaction in transactions_list:
        description = transaction.get("description")
        if description == "Открытие вклада":
            from_ = description
        else:
            from_ = mask_account_card(transaction.get("from"))

        to_ = mask_account_card(transaction.get("to"))
        date = get_date(transaction.get("date"))

        amount = transaction["operationAmount"]["amount"]
        currency = transaction["operationAmount"]["currency"]["name"]

        if description == "Открытие вклада":
            print(f"{date} {description}\nСчет {to_}\nСумма: {amount} {currency}\n")
        else:
            print(f"{date} {description}\n{from_} -> {to_}\nСумма: {amount} {currency}\n")




        if "from" in transactions_list:
            print(f"{mask_account_card(transactions_list.get('to',''))} ->"
                  f"{mask_account_card(transactions_list.get('from',''))}")
        else:
            print(mask_account_card(transactions_list.get('to','')))
            print(f"Сумма: {transactions_list.get('operationAmount','').get('amount','')}"
                  f"{transactions_list.get('operationAmount','').get('currency','')}")