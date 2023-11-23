import datetime
from functools import wraps
from typing import Any, Callable


def log(filename: Any = None) -> Callable:
    """
    Декоратор, который логирует вызов функции в консоль или файл.
    :param filename: принимает необязательный аргумент(если не задан, то логи будут выводиться в консоль)
    :return: Возвращает время записи и состояния лога в консоль или файл
    """

    def wrapper(func: Any) -> Callable:
        @wraps(func)
        def inner(*args: int, **kwargs: int) -> Any:
            try:
                result = func(*args, **kwargs)
                log_message = f"{datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')} {func.__name__} - ok"
            except Exception as error:
                result = None
                log_message = (
                    f"{datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')} {func.__name__} Error: {str(error)}. "
                    f"Inputs: {args}"
                )
            if filename:
                with open(filename, "a") as file:
                    file.write(log_message + "\n")
            else:
                print(log_message)
            return result

        return inner

    return wrapper
