import pytest
from src.masks import card_number, account_number


@pytest.mark.parametrize('user_card, expected', [("7020792289606361", "7020 79** **** 6361"),
                                                 ("4785478523654587", "4785 47** **** 4587"),
                                                 ("1459369826591249", "1459 36** **** 1249"),
                                                 ("9789313251972645", "9789 31** **** 2645")])
def test_card_number(user_card, expected):
    assert card_number(user_card) == expected


@pytest.mark.parametrize('user_invoice, expected', [("73654108430135874305", "**4305"),
                                                    ("63254258496135871598", "**1598"),
                                                    ("12034102396915878520", "**8520"),
                                                    ("11896258102955696918", "**6918")])
def test_account_number(user_invoice, expected):
    assert account_number(user_invoice) == expected
