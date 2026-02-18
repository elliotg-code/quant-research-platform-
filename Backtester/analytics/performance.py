from dataclasses import dataclass
from typing import Dict
import pandas as pd
import numpy as np

TRADING_DAYS = 252

@dataclass
class PerformanceReport:
    total_return: float
    sharpe: float
    sortino: float
    max_drawdown: float
    calmar: float
    turnover: float

class PerformanceAnalyzer:
    def __init__(self, equity_curve: pd.Series, trades: pd.DataFrame):
        self.equity_curve = equity_curve.sort_index()
        self.trades = trades

    def compute(self) -> PerformanceReport:
        returns = self.equity_curve.pct_change().dropna()
        total_return = self.equity_curve.iloc[-1]/self.equity_curve.iloc[0]-1
        sharpe = self._sharpe_ratio(returns)
        sortino = self._sortino_ratio(returns)
        max_dd = self._max_drawdown(self.equity_curve)
        calmar = total_return / abs(max_dd) if max_dd != 0 else np.nan
        turnover = self._turnover()
        return PerformanceReport(total_return, sharpe, sortino, max_dd, calmar, turnover)

    def _sharpe_ratio(self, returns):
        return np.sqrt(TRADING_DAYS) * returns.mean()/returns.std() if returns.std() != 0 else 0

    def _sortino_ratio(self, returns):
        downside = returns[returns < 0]
        return np.sqrt(TRADING_DAYS) * returns.mean()/downside.std() if downside.std() != 0 else 0

    def _max_drawdown(self, equity):
        cumulative_max = equity.cummax()
        drawdown = equity / cumulative_max - 1
        return drawdown.min()

    def _turnover(self):
        if self.trades.empty:
            return 0
        gross_volume = self.trades["quantity"].abs().sum()
        avg_equity = self.equity_curve.mean()
        return gross_volume / avg_equity
