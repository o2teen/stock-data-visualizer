import unittest
from datetime import datetime


# --- Validation Functions (can also live in stock_visualizer.py) ---

def validate_symbol(symbol: str) -> bool:
    """Validates symbol: capitalized, 1-7 alpha characters."""
    if not isinstance(symbol, str):
        return False
    return symbol.isalpha() and symbol.isupper() and (1 <= len(symbol) <= 7)


def validate_chart_type(choice: str) -> bool:
    """Validates chart type: 1 numeric character, 1 or 2."""
    return choice in ["1", "2"]


def validate_time_series(choice: str) -> bool:
    """Validates time series: 1 numeric character, 1 - 4."""
    return choice in ["1", "2", "3", "4"]


def validate_date(date_str: str) -> bool:
    """Validates start/end date: format YYYY-MM-DD."""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except (ValueError, TypeError):
        return False


def validate_date_range(start_date_str: str, end_date_str: str) -> bool:
    """Validates date range logic: start and end are valid, and end >= start."""
    if not validate_date(start_date_str) or not validate_date(end_date_str):
        return False
    start = datetime.strptime(start_date_str, "%Y-%m-%d").date()
    end = datetime.strptime(end_date_str, "%Y-%m-%d").date()
    return end >= start


# --- Unit Test Class ---

class TestStockVisualizerInputs(unittest.TestCase):

    def test_symbol_valid(self):
        self.assertTrue(validate_symbol("AAPL"))
        self.assertTrue(validate_symbol("MSFT"))
        self.assertTrue(validate_symbol("A"))

    def test_symbol_invalid(self):
        self.assertFalse(validate_symbol("aapl"))       # Not capitalized
        self.assertFalse(validate_symbol("AAPL1"))      # Contains numeric
        self.assertFalse(validate_symbol("TOOLONGS"))   # 8 characters (> 7)  <-- Updated here
        self.assertFalse(validate_symbol(""))           # Empty

    def test_chart_type_valid(self):
        self.assertTrue(validate_chart_type("1"))
        self.assertTrue(validate_chart_type("2"))

    def test_chart_type_invalid(self):
        self.assertFalse(validate_chart_type("3"))
        self.assertFalse(validate_chart_type("abc"))
        self.assertFalse(validate_chart_type(""))

    def test_time_series_valid(self):
        self.assertTrue(validate_time_series("1"))
        self.assertTrue(validate_time_series("2"))
        self.assertTrue(validate_time_series("3"))
        self.assertTrue(validate_time_series("4"))

    def test_time_series_invalid(self):
        self.assertFalse(validate_time_series("0"))
        self.assertFalse(validate_time_series("5"))
        self.assertFalse(validate_time_series("daily"))

    def test_start_date_valid(self):
        self.assertTrue(validate_date("2026-01-15"))
        self.assertTrue(validate_date("2023-12-31"))

    def test_start_date_invalid(self):
        self.assertFalse(validate_date("01-15-2026"))   # Wrong format
        self.assertFalse(validate_date("2026-13-01"))   # Invalid month
        self.assertFalse(validate_date("not-a-date"))

    def test_end_date_valid(self):
        self.assertTrue(validate_date("2026-10-31"))

    def test_end_date_invalid(self):
        self.assertFalse(validate_date("2026/10/31"))
        self.assertFalse(validate_date("2026-02-30"))   # Invalid day

    def test_date_range_logic(self):
        self.assertTrue(validate_date_range("2026-01-01", "2026-01-31"))
        self.assertFalse(validate_date_range("2026-01-31", "2026-01-01")) # End before start


if __name__ == "__main__":
    unittest.main()