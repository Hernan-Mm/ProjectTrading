"""Ordered collection of market data observations."""

from src.market_data import MarketData


class MarketDataSeries:
    """Collection of MarketData observations for one instrument."""

    def __init__(self) -> None:
        self._observations: list[MarketData] = []
        self._instrument: str | None = None

    def add(self, observation: MarketData) -> None:
        if not isinstance(observation, MarketData):
            raise TypeError("observation must be a MarketData instance")

        if self._instrument is None:
            self._instrument = observation.instrument
        elif observation.instrument != self._instrument:
            raise ValueError("all observations must use the same instrument")

        self._observations.append(observation)
        self._observations.sort(key=lambda item: item.timestamp)

    def __len__(self) -> int:
        return len(self._observations)

    def __getitem__(self, index: int) -> MarketData:
        if not isinstance(index, int):
            raise TypeError("index must be an integer")
        return self._observations[index]
