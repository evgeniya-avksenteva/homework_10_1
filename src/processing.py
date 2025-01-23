data_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(data_list: list, state: str = "EXECUTED") -> list:
    """Функция принимает список словарей и возвращает новый список словарей,
    содержащий только те словари, у которых ключ state соответствует
    указанному значению"""
    new_data_list = []
    for item_list in data_list:
        if item_list["state"] == state:
            new_data_list.append(item_list)
    return new_data_list


def sort_by_date(data_list: list, sort: bool = True) -> list:
    """Функция возвращает новый список, отсортированный по дате"""

    sorted_data_list = sorted(data_list, key=lambda i: i["date"], reverse=sort)
    return sorted_data_list
