from typing import Generator

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {
            "amount": "43318.34",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {
            "amount": "56883.54",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {
            "amount": "67314.70",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def filter_by_currency(all_transactions: list[dict], currency: str) -> Generator:
    """
    Функцию генератор, которая итерирует список по укаанной валюте
    :param all_transactions: Список со словарями
    :param currency: Указание заданной валюты
    :return: Возвращает итератор, который выдает по очереди операции
    """
    for transaction in all_transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(name_descriptions: list[dict]) -> Generator:
    """
    Функция генератор,которая генерирует описание по каждой опреации
    :param name_descriptions: Список со словарями
    :return: Описание каждой операции по очереди
    """
    for name_description in name_descriptions:
        if name_description in name_descriptions:
            yield name_description["description"]


def card_number_generator(start: int, finish: int) -> Generator:
    """
    Функция генератор, которая генерирует номер банковских карт
    :param start: Начальный диапозон
    :param finish: Конечный диапозон
    :return: Сгенерированые номера карт в заданном диапазоне
    """
    numbers = 16 - len(str(finish))
    for number in range(start, finish + 1):
        generator_num = (numbers * "0") + str(number)
        yield f"{generator_num[0:4]} {generator_num[4:8]} {generator_num[8:12]} {generator_num[12:17]}"
