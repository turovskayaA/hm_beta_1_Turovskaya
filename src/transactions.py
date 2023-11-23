import csv
from typing import Any

import pandas as pd

from data.settings import TRANSACTIONS_EXCEL_PATH, TRANSACTIONS_PATH


def transactions_csv() -> Any:
    """
    Функция, которая считывает финансовые операции с CSV-файлов.
    """
    dict_transaction = []
    with open(TRANSACTIONS_PATH, encoding="UTF-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        for raw in reader:
            dict_transaction.append(raw)
    return dict_transaction


def transactions_excel() -> Any:
    """
    Функция, которая считывает финансовые операции с XLSX-файлов.
    """
    reader_excel = pd.read_excel(TRANSACTIONS_EXCEL_PATH)
    transaction = reader_excel.to_dict("records")
    return transaction
