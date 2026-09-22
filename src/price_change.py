"""Price change calculations for market data observations."""

from decimal import Decimal

from src.market_data import MarketData


def calculate_price_change(
    initial: MarketData, final: MarketData
) -> tuple[Decimal, Decimal]:
    """Return absolute and percentage changes between two observations."""
    if not isinstance(initial, MarketData) or not isinstance(final, MarketData):
        raise TypeError("both observations must be MarketData instances")

    if initial.instrument != final.instrument:
        raise ValueError("observations must use the same instrument")

    initial_price = Decimal(str(initial.price))
    final_price = Decimal(str(final.price))
    absolute_change = final_price - initial_price
    percentage_change = absolute_change / initial_price * 100
    return absolute_change, percentage_change
