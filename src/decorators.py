import datetime

from functools import wraps
from typing import Any


def log(filename: Any) -> Any:
    """
    Декоратор, который логирует вызов функции в консоль или файл.
    :param filename: принимает необязательный аргумент(если не задан, то логи будут выводиться в консоль)
    :return: Возвращает время записи и состояния лога в консоль или файл
    """

    def wrapper(func: Any) -> Any:
        @wraps(func)
        def inner(*args: int, **kwargs: int) -> Any:
            try:
                result = func(*args, **kwargs)
                ok_message = f"{datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')} {func.__name__} - ok"
                print(ok_message)
                if filename:
                    with open(filename, "a") as file:
                        file.write(ok_message + "\n")
            except Exception as error:
                result = None
                error_message = (
                    f"{datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')} {func.__name__} Error: {str(error)}. "
                    f"Inputs: {args}"
                )
                print(error_message)
                if filename:
                    with open(filename, "a") as file:
                        file.write(error_message + "\n")
            return result

        return inner

    return wrapper


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> Any:
    return x / y


my_function(100, 1)
