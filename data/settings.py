from pathlib import Path

ROOT_PATH = Path(__file__).parent
OPERATIONS_PATH = Path.joinpath(ROOT_PATH, "operations.json")
TEST_OPERATIONS_PATH = Path.joinpath(ROOT_PATH, "test_operations.json")
TEST_EMPTY_OPERATIONS_PATH = Path.joinpath(ROOT_PATH, "test_empty_operations.json")
TEST_NOT_FOUND_OPERATIONS_PATH = Path.joinpath(ROOT_PATH, "test_not_found_operations.json")
TRANSACTIONS_PATH = Path.joinpath(ROOT_PATH, "transactions.csv")
TRANSACTIONS_EXCEL_PATH = Path.joinpath(ROOT_PATH, "transactions_excel.xlsx")
