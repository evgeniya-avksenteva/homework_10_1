import pandas as pd
from src.transactions_file import read_transaction_csv, read_transaction_excel
from unittest.mock import mock_open, patch


@patch("builtins.open", new_callable=mock_open, read_data="")
def test_read_transaction_csv(mock_file):
    result_transact = read_transaction_csv("data/transactions.csv")
    assert result_transact == []
    mock_file.assert_called_once_with("data/transactions.csv", mode="r", encoding="utf-8")


def test_read_transaction_csv_invalid_path():
    result_transact = read_transaction_csv("some/invalid/path")
    assert result_transact == []


def test_read_transaction_csv_not_path():
    result_transact = read_transaction_csv("")
    assert result_transact == []


@patch("pandas.read_excel")
def test_read_transaction_excel(mock_read_excel):
    mock_data = pd.DataFrame({"id": ["1", "2", "3"], "Name": ["Sarah", "Mark", "John"]})
    mock_read_excel.return_value = mock_data
    result = read_transaction_excel("fake")
    expected = [
        {"id": "1", "Name": "Sarah"},
        {"id": "2", "Name": "Mark"},
        {"id": "3", "Name": "John"},
    ]
    assert result == expected
