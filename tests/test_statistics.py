import pandas as pd
import numpy as np
from backtester.analytics.statistics import StatisticalValidator

def test_bootstrap_sharpe():
    returns = pd.Series(np.random.normal(0.001, 0.01, 100))
    validator = StatisticalValidator(returns)
    report = validator.bootstrap_sharpe(n_bootstrap=100)
    assert report.sharpe_mean != 0
