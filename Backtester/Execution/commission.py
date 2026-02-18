class FixedCommission:
    def __init__(self, fee: float):
        self.fee = fee

    def calculate(self, quantity: float) -> float:
        return self.fee
