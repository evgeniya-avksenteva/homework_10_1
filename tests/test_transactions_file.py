import pandas as pd
from src.transactions_file import read_transaction_csv, read_transaction_excel
from unittest.mock import patch


def test_read_transaction_csv():
    with patch("pandas.read_csv") as mock_read_csv:
        mock_data = pd.DataFrame(columns=["date", "amount", "description"])
        mock_read_csv.return_value = mock_data
        result = read_transaction_csv("transactions.csv")
        expected_result = []
        assert result == expected_result
        mock_read_csv.assert_called_once_with("transactions.csv", sep=";")


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
