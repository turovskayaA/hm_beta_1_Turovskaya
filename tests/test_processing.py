import pytest
from src.processing import filter_state, sort_date


@pytest.fixture
def data_list():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_state(data_list):
    assert filter_state(data_list) == [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                                       {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}]
    assert (filter_state(data_list, "CANCELED") ==
            [{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}])


def test_sort_date(data_list):
    assert sort_date(data_list) == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                                    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
    assert (sort_date(data_list, False) ==
            [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}])



