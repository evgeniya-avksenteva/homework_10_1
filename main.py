import os

from src.banking_operations import search_transactions
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.transactions_file import read_transaction_csv, read_transaction_excel
from src.utils import financial_transactions
from src.widget import get_date, mask_account_card


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
            print("Для обработки выбран JSON-файл.")
            transactions_list = financial_transactions(os.path.join("data", "operations.json"))
            break
        elif user_file_choice == "2":
            print("Для обработки выбран CSV-файл.")
            transactions_list = read_transaction_csv(os.path.join("data", "transactions.csv"))
            break
        elif user_file_choice == "3":
            print("Для обработки выбран XLSX-файл.")
            transactions_list = read_transaction_excel(os.path.join("data", "transactions_excel.xlsx"))
            break
        else:
            print("Некорректный выбор. Попробуй еще раз.")
            continue

    while True:
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING:\n"
        ).upper()
        if status in ["CANCELED", "PENDING", "EXECUTED"]:
            transactions_list = filter_by_state(transactions_list, status)
            print(f'Операции отфильтрованы по статусу "{status}"')
            break
        else:
            print(f'Статус операции "{status}" недоступен')

    while True:
        sort_date = input("Отсортировать операции по дате? Да/Нет\n").lower()
        if sort_date == "да":
            while True:
                sorting_order = input(
                    """Отсортировать по возрастанию или по убыванию? по возрастанию/по убыванию\n"""
                ).lower()
                if sorting_order == "по возрастанию":
                    transactions_list = sort_by_date(transactions_list, False)
                    break
                elif sorting_order == "по убыванию":
                    transactions_list = sort_by_date(transactions_list, True)
                    break
                else:
                    print("Некорректный выбор. Попробуйте еще раз.")
                    continue
            break
        elif sort_date == "нет":
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")

    while True:
        sort_code = str(input("Выводить только рублевые транзакции? Да/Нет\n")).lower()
        if sort_code == "да":
            if user_file_choice == "1":
                transactions_list = list(filter_by_currency(transactions_list, "RUB"))
            else:
                transactions_list = list(filter_by_currency(transactions_list, "RUB", False))
            break
        elif sort_code == "нет":
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")

    while True:
        user_input = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет:\n").lower()
        if user_input == "да":
            search = input("Видите слово для поиска: ")
            transactions_list = search_transactions(transactions_list, search)
            break
        elif user_input == "нет":
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")

    transactions = list(transactions_list)

    print("Распечатываю итоговый список транзакций...")

    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return
    else:
        print(f"Всего банковских операций в выборке: {len(transactions)}")

    for transaction in transactions:
        description = transaction.get("description")
        if description == "Открытие вклада":
            from_ = description
        else:
            from_ = mask_account_card(transaction.get("from"))

        to_ = mask_account_card(transaction.get("to"))
        date = get_date(transaction.get("date"))

        if user_file_choice == "1":
            amount = transaction["operationAmount"]["amount"]
            currency = transaction["operationAmount"]["currency"]["name"]
        else:
            amount = transaction["amount"]
            currency = transaction["currency_code"]

        if description == "Открытие вклада":
            print(f"{date} {description}\nСчет {to_}\nСумма: {amount} {currency}\n")
        else:
            print(f"{date} {description}\n{from_} -> {to_}\nСумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()
