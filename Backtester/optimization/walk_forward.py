import pandas as pd
from typing import Callable, Dict, List

class WalkForwardValidator:
    def __init__(self, data: pd.DataFrame, train_period: int, test_period: int):
        self.data = data
        self.train_period = train_period
        self.test_period = test_period

    def run(self, strategy_factory: Callable[[Dict], object], param_grid: List[Dict], evaluation_fn: Callable[[pd.DataFrame], float]):
        results = []
        start = 0
        while start+self.train_period+self.test_period <= len(self.data):
            train_data = self.data.iloc[start:start+self.train_period]
            test_data = self.data.iloc[start+self.train_period:start+self.train_period+self.test_period]

            best_score = float("-inf")
            best_params = None
            for params in param_grid:
                strategy = strategy_factory(params)
                equity = strategy.backtest(train_data)
                score = evaluation_fn(equity)
                if score > best_score:
                    best_score = score
                    best_params = params

            test_strategy = strategy_factory(best_params)
            test_equity = test_strategy.backtest(test_data)
            test_score = evaluation_fn(test_equity)

            results.append({"start": start, "params": best_params, "train_score": best_score, "test_score": test_score})
            start += self.test_period

        return pd.DataFrame(results)
