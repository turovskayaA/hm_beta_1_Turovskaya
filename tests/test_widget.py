import pytest

from src.widget import datatime, type_card_and_account_number


@pytest.mark.parametrize(
    "name_and_masks, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Master Card 7158300734726758", "Master Card 7158 30** **** 6758"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Счет 35383033474447895560", "Счет **5560"),
    ],
)
def test_type_card_and_account_number(name_and_masks, expected):
    assert type_card_and_account_number(name_and_masks) == expected


@pytest.mark.parametrize("data_time, date", [("2018-07-11T02:26:18.671407", "11.07.2018")])
def test_datatime(data_time, date):
    assert datatime(data_time) == date
