import json
import logging
from typing import Any

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
console_handler = logging.FileHandler(filename="my_loggin.log", mode="w")
console_formatter = logging.Formatter(
    "%(asctime)s %(module)s %(levelname)s: %(message)s"
)
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)
logger.setLevel(logging.DEBUG)


def transaction(operation: Any) -> Any:
    """
    Функцию, которая принимает на вход путь до JSON-файла.
    :return: Возвращает список словарей с данными о финансовых транзакциях.
    """
    try:
        with open(operation, encoding="UTF-8") as file:
            operation = json.load(file)
    except FileNotFoundError:
        logger.error(f"Ошибка типа: {FileNotFoundError}")
        operation = []
    except json.JSONDecodeError:
        logger.error(f"Ошибка типа: {json.JSONDecodeError}")
        operation = []
    return operation


def transaction_rub(operation: dict[str, Any]) -> Any:
    """
    Функцию, которая принимает на вход одну транзакцию.
    :param operation: Список словарей с данными о финансовых транзакциях
    :return: Вовращает сумму транзакции в рублях или ошибку ValueError
    """
    if operation["operationAmount"]["currency"]["code"] == "RUB":
        logger.info(
            f"Сумма транзакиции в рублях: {operation['operationAmount']['amount']}"
        )
        return operation["operationAmount"]["amount"]
    else:
        logger.error(
            ValueError("Транзация выполнена не в рублях. Укажите транзакцию в рублях")
        )
        raise ValueError("Транзация выполнена не в рублях. Укажите транзакцию в рублях")
