"""Internal representation of a single market data observation."""

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal, InvalidOperation
from numbers import Number
from typing import Any


def _as_finite_decimal(value: Any, field_name: str) -> Decimal:
    if isinstance(value, bool) or not isinstance(value, Number):
        raise TypeError(f"{field_name} must be numeric")

    try:
        decimal_value = Decimal(str(value))
    except (InvalidOperation, ValueError):
        raise ValueError(f"{field_name} must be finite") from None

    if not decimal_value.is_finite():
        raise ValueError(f"{field_name} must be finite")

    return decimal_value


@dataclass(frozen=True)
class MarketData:
    """Immutable market observation independent of any data provider."""

    instrument: str
    timestamp: datetime
    price: Number
    volume: Number

    def __post_init__(self) -> None:
        if not isinstance(self.instrument, str) or not self.instrument.strip():
            raise ValueError("instrument must be a non-empty string")

        if not isinstance(self.timestamp, datetime):
            raise TypeError("timestamp must be a datetime")
        if self.timestamp.tzinfo is None or self.timestamp.utcoffset() is None:
            raise ValueError("timestamp must include timezone information")

        price = _as_finite_decimal(self.price, "price")
        if price <= 0:
            raise ValueError("price must be positive")

        volume = _as_finite_decimal(self.volume, "volume")
        if volume < 0:
            raise ValueError("volume must be non-negative")