import datetime

from src.decorators import log


@log(filename="mylog.txt")
def test_function():
    def my_function(x, y):
        return x / y
    date_time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    assert my_function(100, 1) == f"{date_time} my_function - ok"
    assert my_function(100, 0) == f"{date_time} my_function Error: division by zero. Inputs: (100, 0)"


