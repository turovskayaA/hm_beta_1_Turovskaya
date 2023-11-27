import re
from collections import Counter
from typing import Dict, List


def search_operations(
        transactions: List[Dict[str, str]], string: str
) -> List[Dict[str, str]]:
    """
     Фильтрует список операций по описанию.
    :param transactions: Список словарей с данными о банковских операциях.
    :param string: Строка для поиска в описании операций.
    :return: Отфильтрованный список операций.
    """
    result = []
    for transaction in transactions:
        if re.search(string, transactions.get("description", ""), re.IGNORECASE):
            result.append(transaction)
    return result


def count_operations(
        transactions: List[Dict[str, str]], categories: Dict[str, str]
) -> Counter:
    """
     Создает Counter с количеством операций в каждой категории.
    :param transactions: Список словарей с данными о банковских операциях.
    :param categories: Словарь категорий операций.
    :return: Количество операций в каждой категории.
    """
    counted = Counter(
        transactions.get("category", "")
        for transaction in transactions
        if transaction.get("category", "") in categories
    )
    return counted
