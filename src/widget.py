import maya
from typing import Any
from masks import card_number, account_number


def type_card_and_account_number(type_and_number: str) -> str:
    """
    Функция маскировки типа карта/счета с номером.
    :param type_and_number: Номер и тип(карта/счет) для маскирования
    :return: Маскированный по правилу тип и номер
    """
    split_number = type_and_number.split()
    if "счет" in split_number:
        number = split_number[-1]
        masks_number = account_number(number)
        name_and_masks = split_number[0], masks_number
        return " ".join(name_and_masks)
    else:
        number = split_number[-1]
        masks_number = card_number(number)
        name_and_masks = split_number[0], masks_number
        return " ".join(name_and_masks)


def datatime(data: str) -> Any:
    """
    Функция преобразовании времени и даты
    :param data: Время и дату
    :return: Дату
    """
    data_and_time = maya.parse(data).datetime()
    return data_and_time.date()


def main():
    user_type_and_number = str(input("Введите тип карты/счета и ее номер:")).lower()
    print(type_card_and_account_number(user_type_and_number))

    user_datatime = "2018-07-11T02:26:18.671407"
    print(datatime(user_datatime))


if __name__ == "__main__":
    main()
