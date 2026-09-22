import unittest
from datetime import datetime, timezone
from decimal import Decimal

from src.market_data import MarketData


class MarketDataTests(unittest.TestCase):
    def setUp(self) -> None:
        self.timestamp = datetime(2026, 9, 22, 12, 0, tzinfo=timezone.utc)

    def test_creates_valid_data_and_preserves_values(self) -> None:
        market_data = MarketData("AAPL", self.timestamp, Decimal("150.25"), 100)

        self.assertEqual(market_data.instrument, "AAPL")
        self.assertEqual(market_data.timestamp, self.timestamp)
        self.assertEqual(market_data.price, Decimal("150.25"))
        self.assertEqual(market_data.volume, 100)

    def test_rejects_invalid_instrument(self) -> None:
        with self.assertRaises(ValueError):
            MarketData("  ", self.timestamp, 10, 1)

    def test_rejects_invalid_timestamp(self) -> None:
        with self.assertRaises((TypeError, ValueError)):
            MarketData("AAPL", datetime(2026, 9, 22, 12, 0), 10, 1)

    def test_rejects_invalid_price(self) -> None:
        with self.assertRaises((TypeError, ValueError)):
            MarketData("AAPL", self.timestamp, 0, 1)

    def test_rejects_negative_volume(self) -> None:
        with self.assertRaises(ValueError):
            MarketData("AAPL", self.timestamp, 10, -1)

    def test_is_immutable(self) -> None:
        market_data = MarketData("AAPL", self.timestamp, 10, 1)

        with self.assertRaises(AttributeError):
            market_data.price = 11


if __name__ == "__main__":
    unittest.main()