import pandas as pd


def read_transaction_csv(file_csv: str) -> list:
    """Функция считывает финансовые операции из CSV"""
    reader = pd.read_csv(file_csv, sep=";")
    return reader.to_dict(orient="records")


# if __name__ == "__main__":
#     result_excel = read_transaction_csv("../data/transactions.csv")
#     print(result_excel)


def read_transaction_excel(file_excel: str) -> list:
    """Функция считывает финансовые операции из Excel"""
    df = pd.read_excel(file_excel)
    transactions_excel = df.to_dict(orient="records")
    return transactions_excel


# if __name__ == "__main__":
#    result_excel = read_transaction_excel("../data/transactions_excel.xlsx")
#    print(result_excel[3])
