import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

@pytest.fixture
def transactions():
    return [
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


def test_filter_by_currency(transactions: list[dict], currency: str = "USD") -> iter:
    if currency == "USD":
        assert test_filter_by_currency(transactions) == [
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 73654108430135874305",
            "to": "Счет 11776614605963066702"},
            {"id": 142264268, "state": "EXECUTED", "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 73654108430135874305",
            "to": "Счет 75651667383060284188"},
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Platinum 7000792289606361",
            "to": "Visa Classic 8990922113665229"}
        ]

    elif currency == "RUB":
        assert filter_by_currency(transactions) == [
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "RUB", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 73654108430135874305",
            "to": "Счет 74489636417521191160"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "RUB", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 7000792289606361",
            "to": "Счет 74489636417521191160"}
        ]



def test_transaction_descriptions(transactions: list[dict]) -> None:
    #тестирование функции описания
    assert transaction_descriptions(transactions[0]) ==  "Перевод организации"


def test_card_number_generator(start: str, stop: str) -> str:
    assert card_number_generator(1, 1) == "0000 0000 0000 0001"

