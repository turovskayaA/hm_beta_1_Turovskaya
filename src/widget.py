from masks import card_number, account_number


def type_card_and_account_number(type_and_number: str) -> str:
    """
    Функция маскировки типа карта/счета с номером.
    :param type_and_number: Номер и тип(карта/счет) для маскирования
    :return: Маскированный по правилу тип и номер
    """
    split_number = type_and_number.split()
    if "Счет" in split_number:
        number = split_number[-1]
        masks_number = account_number(number)
        name_and_masks = split_number[0], masks_number
        return " ".join(name_and_masks)
    else:
        number = split_number[-1]
        name_card = " ".join(split_number[:-1])
        masks_number = card_number(number)
        name_and_masks = name_card, masks_number
        return " ".join(name_and_masks)


def datatime(data: str) -> str:
    """
    Функция преобразовании времени и даты
    :param data: Время и дату
    :return: Дату
    """
    return f'{data[8:10]}.{data[5:7]}.{data[0:4]}'


def main():
    user_type_and_number = str(input("Введите тип карты/счета и ее номер:")).title()
    print(type_card_and_account_number(user_type_and_number))

    user_datatime = "2018-07-11T02:26:18.671407"
    print(datatime(user_datatime))


if __name__ == "__main__":
    main()
