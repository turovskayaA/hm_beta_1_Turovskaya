import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
console_handler = logging.FileHandler(filename="my_loggin.log", mode="w")
console_formatter = logging.Formatter(
    "%(asctime)s %(module)s %(levelname)s: %(message)s"
)
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)
logger.setLevel(logging.DEBUG)


def card_number(number: str) -> str:
    """
    Функция маскировки карты.
    :param number: Номер для маскирования
    :return: Маскированный по правилу номер карты
    """
    stars = number[0:6] + ("*" * len(number[6:12])) + number[12:16]
    total = " ".join([stars[i : i + 4] for i in range(0, len(number), 4)])
    logger.info(f"Замаскированный номер карты: {total}")
    return total


def account_number(number: str) -> str:
    """
    Функция маскировки номера счёта.
    :param number: Номер для маскирования
    :return: Маскированный по правилу номер счёта
    """
    stars = "**" + number[-4:]
    logger.info(f"Замаскированный номер счета: {stars}")
    return stars


user_card = "7020792289606361"
print(card_number(user_card))
user_invoice = "73654108430135874305"
print(account_number(user_invoice))
