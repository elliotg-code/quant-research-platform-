import numpy as np
import pandas as pd
from dataclasses import dataclass

TRADING_DAYS = 252

@dataclass
class BootstrapReport:
    sharpe_mean: float
    sharpe_ci_lower: float
    sharpe_ci_upper: float
    prob_sharpe_positive: float

class StatisticalValidator:
    def __init__(self, returns: pd.Series):
        self.returns = returns.dropna().values

    def bootstrap_sharpe(self, n_bootstrap=1000, confidence=0.95):
        sharpe_samples = []
        for _ in range(n_bootstrap):
            sample = np.random.choice(self.returns, size=len(self.returns), replace=True)
            sharpe_samples.append(self._sharpe(sample))
        sharpe_samples = np.array(sharpe_samples)
        lower = np.percentile(sharpe_samples, (1-confidence)/2*100)
        upper = np.percentile(sharpe_samples, (1+confidence)/2*100)
        return BootstrapReport(
            sharpe_mean=sharpe_samples.mean(),
            sharpe_ci_lower=lower,
            sharpe_ci_upper=upper,
            prob_sharpe_positive=(sharpe_samples > 0).mean()
        )

    def monte_carlo_equity(self, initial_capital=1_000_000, n_simulations=1000):
        simulations = []
        for _ in range(n_simulations):
            shuffled = np.random.permutation(self.returns)
            equity = initial_capital * np.cumprod(1+shuffled)
            simulations.append(equity)
        return pd.DataFrame(simulations).T

    def _sharpe(self, returns):
        return np.sqrt(TRADING_DAYS) * returns.mean()/returns.std() if returns.std()!=0 else 0
