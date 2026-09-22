import unittest
from datetime import datetime, timedelta, timezone

from src.market_data import MarketData
from src.market_data_series import MarketDataSeries


class MarketDataSeriesTests(unittest.TestCase):
    def setUp(self) -> None:
        self.start = datetime(2026, 9, 22, 12, 0, tzinfo=timezone.utc)

    def make_observation(self, minutes: int, instrument: str = "AAPL") -> MarketData:
        return MarketData(
            instrument,
            self.start + timedelta(minutes=minutes),
            100 + minutes,
            10,
        )

    def test_creates_empty_series(self) -> None:
        series = MarketDataSeries()

        self.assertEqual(len(series), 0)

    def test_adds_valid_observation(self) -> None:
        series = MarketDataSeries()
        observation = self.make_observation(1)

        series.add(observation)

        self.assertEqual(len(series), 1)
        self.assertIs(series[0], observation)

    def test_keeps_observations_in_chronological_order(self) -> None:
        series = MarketDataSeries()
        later = self.make_observation(2)
        earlier = self.make_observation(1)

        series.add(later)
        series.add(earlier)

        self.assertIs(series[0], earlier)
        self.assertIs(series[1], later)

    def test_rejects_non_market_data_observation(self) -> None:
        series = MarketDataSeries()

        with self.assertRaises(TypeError):
            series.add("not market data")

    def test_rejects_different_instrument(self) -> None:
        series = MarketDataSeries()
        series.add(self.make_observation(1, "AAPL"))

        with self.assertRaises(ValueError):
            series.add(self.make_observation(2, "MSFT"))

    def test_supports_index_access(self) -> None:
        series = MarketDataSeries()
        observation = self.make_observation(1)
        series.add(observation)

        self.assertIs(series[0], observation)

    def test_does_not_allow_external_collection_mutation(self) -> None:
        series = MarketDataSeries()
        observation = self.make_observation(1)
        series.add(observation)

        with self.assertRaises(TypeError):
            series[0] = self.make_observation(2)

        self.assertEqual(len(series), 1)
        self.assertIs(series[0], observation)


if __name__ == "__main__":
    unittest.main()
