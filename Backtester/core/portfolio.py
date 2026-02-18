from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Position:
    quantity: float = 0.0
    avg_price: float = 0.0


@dataclass
class Portfolio:
    cash: float
    positions: Dict[str, Position] = field(default_factory=dict)

    def update_fill(self, symbol: str, quantity: float, price: float) -> None:
        cost = quantity * price
        self.cash -= cost

        position = self.positions.get(symbol, Position())
        new_qty = position.quantity + quantity

        if new_qty != 0:
            position.avg_price = (
                (position.quantity * position.avg_price + quantity * price)
                / new_qty
            )

        position.quantity = new_qty
        self.positions[symbol] = position
