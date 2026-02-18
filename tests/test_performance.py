import pandas as pd
from backtester.analytics.performance import PerformanceAnalyzer

def test_sharpe_positive():
    equity = pd.Series([100,101,102,103,104])
    trades = pd.DataFrame(columns=["quantity"])
    analyzer = PerformanceAnalyzer(equity, trades)
    report = analyzer.compute()
    assert report.sharpe > 0

def test_max_drawdown_zero_when_monotonic():
    equity = pd.Series([100,101,102,103])
    trades = pd.DataFrame(columns=["quantity"])
    analyzer = PerformanceAnalyzer(equity, trades)
    report = analyzer.compute()
    assert report.max_drawdown == 0
