import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("masks_log.log", "w")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция, которая принимает на вход номер карты
    и возвращает маску номера"""
    logger.error("Создание маски номера карты")
    if len(card_number) != 16:
        logger.error("Номер карты состоит из 16 цифр")
        raise ValueError("Номер карты состоит из 16 цифр")
    logger.info("Маска номера карты создана")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(account_number: str) -> str:
    """Функция, которая принимает на вход номер счета
    и возвращает маску номера"""
    logger.info("Создание маски номера счета")
    logger.info("Маска номера счета создана")
    return f"**{account_number[-4:]}"


# if __name__ == "__main__":
#    print(get_mask_card_number("7000792289606361"))
#    print(get_mask_account("73654108430135874305"))
