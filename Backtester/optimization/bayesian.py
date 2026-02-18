import numpy as np
from typing import Callable, Dict, Tuple

class BayesianOptimizer:
    def __init__(self, param_bounds: Dict[str, Tuple[float,float]], objective_fn: Callable[[Dict], float], n_iter=30, random_state=42):
        self.param_bounds = param_bounds
        self.objective_fn = objective_fn
        self.n_iter = n_iter
        self.random_state = np.random.RandomState(random_state)

    def optimize(self):
        best_params = None
        best_score = float("-inf")
        for _ in range(self.n_iter):
            params = {key: self.random_state.uniform(low, high) for key,(low,high) in self.param_bounds.items()}
            score = self.objective_fn(params)
            if score > best_score:
                best_score = score
                best_params = params
        return {"best_params": best_params, "best_score": best_score}
