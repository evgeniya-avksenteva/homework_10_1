import csv
import pandas as pd
from typing import Any, Dict, List


def read_transaction_csv(file_csv: str) -> List[Dict[str, Any]]:
    transactions_csv = []
    """Функция считывает финансовые операции из CSV"""
    try:
        with open(file_csv, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                transactions_csv.append(row)
        return transactions_csv
    except Exception:
        return []


# if __name__ == "__main__":
#     result_csv = read_transaction_csv("../data/transactions.csv")
#     print(result_csv[2])


def read_transaction_excel(file_excel: str) -> list:
    """Функция считывает финансовые операции из Excel"""
    df = pd.read_excel(file_excel)
    transactions_excel = df.to_dict(orient="records")
    return transactions_excel


# if __name__ == "__main__":
#    result_excel = read_transaction_excel("../data/transactions_excel.xlsx")
#    print(result_excel[3])
