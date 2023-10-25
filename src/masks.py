def card_number(number: str) -> str:
    """
    Функция маскировки карты.
    :param number: Номер для маскирования
    :return: Маскированный по правилу номер карты
    """
    stars = number[0:6] + ("*" * len(number[6:12])) + number[12:16]
    return " ".join([stars[i: i + 4] for i in range(0, len(number), 4)])


def account_number(number: str) -> str:
    """
    Функция маскировки номера счёта.
    :param number: Номер для маскирования
    :return: Маскированный по правилу номер счёта
    """
    stars = "**" + number[-4:]
    return stars


def main():
    user_card = str(input("Номер карты: "))
    print(card_number(user_card))
    user_invoice = str(input("Номер счета: "))
    print(account_number(user_invoice))


if __name__ == "__main__":
    main()
