from backtester.execution.slippage import PercentageSlippage
from backtester.execution.commission import FixedCommission


class Broker:
    def __init__(self, slippage: PercentageSlippage, commission: FixedCommission):
        self.slippage = slippage
        self.commission = commission

    def execute_order(self, symbol: str, quantity: float, price: float):
        is_buy = quantity > 0
        exec_price = self.slippage.apply(price, is_buy)
        fee = self.commission.calculate(quantity)
        return exec_price, fee
