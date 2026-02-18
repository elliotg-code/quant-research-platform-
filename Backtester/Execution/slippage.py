class PercentageSlippage:
    def __init__(self, pct: float):
        self.pct = pct

    def apply(self, price: float, is_buy: bool) -> float:
        return price * (1 + self.pct if is_buy else 1 - self.pct)
