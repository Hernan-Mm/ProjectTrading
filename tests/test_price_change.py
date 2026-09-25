import unittest
from datetime import datetime, timedelta, timezone
from decimal import Decimal

from src.market_data import MarketData
from src.price_change import calculate_price_change


class PriceChangeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.start = datetime(2026, 9, 22, 12, 0, tzinfo=timezone.utc)

    def make_observation(self, price: object, minutes: int = 0) -> MarketData:
        return MarketData(
            "AAPL",
            self.start + timedelta(minutes=minutes),
            price,
            10,
        )

    def test_calculates_price_increase(self) -> None:
        initial = self.make_observation(100)
        final = self.make_observation(125, 1)

        absolute_change, _ = calculate_price_change(initial, final)

        self.assertEqual(absolute_change, Decimal("25"))

    def test_calculates_price_decrease(self) -> None:
        initial = self.make_observation(100)
        final = self.make_observation(75, 1)

        absolute_change, _ = calculate_price_change(initial, final)

        self.assertEqual(absolute_change, Decimal("-25"))

    def test_calculates_percentage_change(self) -> None:
        initial = self.make_observation(100)
        final = self.make_observation(125, 1)

        _, percentage_change = calculate_price_change(initial, final)

        self.assertEqual(percentage_change, Decimal("25"))

    def test_calculates_negative_percentage_change(self) -> None:
        initial = self.make_observation(100)
        final = self.make_observation(75, 1)

        _, percentage_change = calculate_price_change(initial, final)

        self.assertEqual(percentage_change, Decimal("-25"))

    def test_calculates_no_price_change(self) -> None:
        initial = self.make_observation(100)
        final = self.make_observation(100, 1)

        absolute_change, percentage_change = calculate_price_change(initial, final)

        self.assertEqual(absolute_change, Decimal("0"))
        self.assertEqual(percentage_change, Decimal("0"))

    def test_allows_observations_with_equal_timestamps(self) -> None:
        initial = self.make_observation(100)
        final = self.make_observation(125)

        absolute_change, percentage_change = calculate_price_change(initial, final)

        self.assertEqual(absolute_change, Decimal("25"))
        self.assertEqual(percentage_change, Decimal("25"))

    def test_rejects_final_observation_before_initial(self) -> None:
        initial = self.make_observation(100)
        final = self.make_observation(125, -1)

        with self.assertRaises(ValueError):
            calculate_price_change(initial, final)

    def test_rejects_incorrect_types(self) -> None:
        observation = self.make_observation(100)

        with self.assertRaises(TypeError):
            calculate_price_change(observation, "not market data")

    def test_rejects_different_instruments(self) -> None:
        initial = self.make_observation(100)
        final = MarketData("MSFT", self.start + timedelta(minutes=1), 125, 10)

        with self.assertRaises(ValueError):
            calculate_price_change(initial, final)


if __name__ == "__main__":
    unittest.main()
