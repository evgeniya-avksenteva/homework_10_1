import pytest
from src.generators import card_number_generator, transaction_descriptions, filter_by_currency


if __name__ == "__main__":
    pytest.main()


@pytest.fixture
def transactions_1() -> str:
    """Тестирование функции на корректную фильтрацию транзакций по заданной валюте"""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
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
                "currency": {"name": "USD", "code": "USD"},
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
                "currency": {"name": "RUB", "code": "RUB"},
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
                "currency": {"name": "USD", "code": "USD"},
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
                "currency": {"name": "RUB", "code": "RUB"},
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 7000792289606361",
            "to": "Счет 74489636417521191160",
        },
    ]


def test_filter_by_currency(transactions_1: list[dict[str]]) -> None:
    usd_generator = filter_by_currency(transactions_1, "USD")
    assert next(usd_generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 73654108430135874305",
        "to": "Счет 11776614605963066702",
    }
    assert next(usd_generator) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 73654108430135874305",
        "to": "Счет 75651667383060284188",
    }
    assert next(usd_generator) == {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Platinum 7000792289606361",
        "to": "Visa Classic 8990922113665229",
    }


@pytest.fixture
def transactions_2() -> str:
    """Тестирование, чтобы функция возвращала корректные описания для каждой транзакции"""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
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
                "currency": {"name": "USD", "code": "USD"},
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
                "currency": {"name": "RUB", "code": "RUB"},
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
                "currency": {"name": "USD", "code": "USD"},
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
                "currency": {"name": "RUB", "code": "RUB"},
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 7000792289606361",
            "to": "Счет 74489636417521191160",
        },
    ]


def test_transaction_descriptions(transactions_2: list[dict]) -> str:
    generator = transaction_descriptions(transactions_2)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"


@pytest.mark.parametrize(
    "start, stop, card_number",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        )
    ],
)
def test_card_number_generator(start, stop, card_number) -> None:
    """Тестирование, которое проверяет, что генератор выдает правильные номера карт в заданном диапазоне"""
    result = []
    for i in card_number_generator(start, stop):
        result.append(i)
    print(result)
    assert result == card_number
