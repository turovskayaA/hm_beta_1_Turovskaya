import json
from typing import Any


def transaction(operation: Any) -> Any:
    """
    Функцию, которая принимает на вход путь до JSON-файла.
    :return: Возвращает список словарей с данными о финансовых транзакциях.
    """
    try:
        with open(operation, encoding="UTF-8") as file:
            operation = json.load(file)
    except FileNotFoundError:
        operation = []
    except json.JSONDecodeError:
        operation = []
    return operation


def transaction_rub(operation: dict[str, Any]) -> Any:
    """
    Функцию, которая принимает на вход одну транзакцию.
    :param operation: Список словарей с данными о финансовых транзакциях
    :return: Вовращает сумму транзакции в рублях или ошибку ValueError
    """
    if operation["operationAmount"]["currency"]["code"] == "RUB":
        return operation["operationAmount"]["amount"]
    else:
        raise ValueError("Транзация выполнена не в рублях. Укажите транзакцию в рублях")
