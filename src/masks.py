def get_mask_card_number(card_number: str) -> str:
    """Функция, которая принимает на вход номер карты
    и возвращает маску номера"""
    if len(card_number) != 16:
        raise ValueError("Номер карты состоит из 16 цифр")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(account_number: str) -> str:
    """Функция, которая принимает на вход номер счета
    и возвращает маску номера"""
    return f"**{account_number[-4:]}"


print(get_mask_card_number("7000792289606361"))
print(get_mask_account("73654108430135874305"))
