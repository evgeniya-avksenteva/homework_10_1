import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("number_card_or_score_account, mask_card_number",
                       [('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
                        ('Maestro 7000792289606361', 'Maestro 7000 79** **** 6361'),
                        ('Счет 73654108430135874305', 'Счет **4305')])

def test_mask_account_card(number_card_or_score_account, mask_card_number):
    assert mask_account_card(number_card_or_score_account) == mask_card_number


@pytest.fixture
def fixture_date():
    return ["2024-03-11T02:26:18.671407", "11.03.2024"]


@pytest.mark.parametrize("date_test, expected", [('2024-03-11T02:26:18.671407', '11.03.2024'),
    ('2024-05-15T02:26:10.671407', '15.05.2024')])
def test_get_date(date_test, expected):
    assert get_date(date_test) == expected
