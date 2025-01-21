from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card: str) -> str:
    """Функция, которая обрабатывает информацию по карте или счету"""
    if "Счет" in card:
        return "Счет " + get_mask_account(card)
    else:
        cards = get_mask_card_number(card[-16:])
        new_card = card.replace(card[-16:], cards)
        return new_card


def get_date(date: str) -> str:
    """Функция, которая возвращает строку с датой в определенном формате"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
