import unittest.mock as mock
import pandas as pd

from src.transactions import transactions_csv, transactions_excel


def test_transactions_cvs():
    with mock.patch("src.transactions.csv.DictReader") as mock_reader_cvs:
        mock_reader_cvs.return_value = [{'id': "1", "description": "Перевод организации"}]
        result = transactions_csv()
    assert result == [{'id': "1", "description": "Перевод организации"}]


def test_transactions_xlsx():
    with mock.patch("src.transactions.pd.read_excel") as mock_reader_excel:
        mock_reader_excel.return_value = pd.DataFrame([{'id': 1, "description": "Перевод организации"}])
        result = transactions_excel()
    assert result == [{'id': 1, "description": "Перевод организации"}]
