def filter_state(info: list, state="EXECUTED") -> list:
    """
    Функция, которая принимает на вход список словарей и значение для ключа state
    :param info: список со словарями
    :param state: ключ в словаре
    :return: возвращает новый список, содержащий только те словари, у которых ключ state
             содержит переданное в функцию значение
    """
    filter_dict = []
    for item in info:
        if item.get("state") == state:
            filter_dict.append(item)
    return filter_dict


def sort_date(sorted_date: list) -> list:
    """
    Функцию, которая принимает на вход список словарей для ее отсортировки по дате
    :param sorted_date:список со словарями
    :return:возвращает новый список,
            в котором исходные словари отсортированы по убыванию даты
    """
    date = sorted(sorted_date, key=lambda info_date: info_date["date"], reverse=True)
    return date


def main():
    input_info = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    print(f"Отсортировка по значанию 'state': {filter_state(input_info,'CANCELED')}")
    print(f"Отсортировка по значанию 'date': {sort_date(input_info)}")


if __name__ == "__main__":
    main()
