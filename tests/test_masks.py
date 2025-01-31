import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number() -> None:
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


def test_invalid_card_number() -> None:
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("70007922896063610")
    assert str(exc_info.value) == "Номер карты состоит из 16 цифр"


def test_get_mask_account() -> None:
    assert get_mask_account("73654108430135874305") == "**4305"
