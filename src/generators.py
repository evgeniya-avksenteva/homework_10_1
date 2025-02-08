transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            },
        },
        "description": "Перевод организации",  #
        "from": "Счет 73654108430135874305",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "USD",
                "code": "USD"
            },
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 73654108430135874305",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {
            "amount": "43318.34",
            "currency": {
                "name": "RUB",
                "code": "RUB"
            },
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 73654108430135874305",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "56883.54",
            "currency": {
                "name": "USD",
                "code": "USD"
            },
        },
        "description": "Перевод с карты на карту",
        "from": "Visa Platinum 7000792289606361",
        "to": "Visa Classic 8990922113665229",
    },
    {
        "id": 615064591,
        "state": "CANCELED",
        "date": "2018-10-14T08:21:33.419441",
        "operationAmount": {
            "amount": "67314.70",
            "currency": {
                "name": "RUB",
                "code": "RUB"
            },
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 7000792289606361",
        "to": "Счет 74489636417521191160"
    },
]


def filter_by_currency(transactions: list[dict], currency: str = "USD") -> iter:
    """ Функция принимает список транзакций и возвращает итератор,
    где валюта операции соответствует заданной """
    return (item for item in transactions if item["operationAmount"]["currency"]["code"] == currency)

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(3):
    print(next(usd_transactions))


def transaction_descriptions(transactions: list[dict]) -> None:
    """ Функция принимает список транзакций и возвращает описание
    каждой операции по заданным значениям """
    for x in transactions:
        yield x.get("description")

descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))


def card_number_generator(start: str,stop: str) -> str:
    """ Генератор принимает начальное и конечное значение
    для генерации диапазона номеров """
    for i in range (start, stop+1):
        start_str = "0000000000000000"
        sum_str = start_str + str(i)
        card_number = f"{sum_str[-16:-12]} {sum_str[-12:-8]} {sum_str[-8:-4]} {sum_str[-4:-1]}{sum_str[-1]}"
        yield card_number

for card_number in card_number_generator(1, 5):
        print(card_number)
