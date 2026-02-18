from itertools import product
from typing import Dict, List

def generate_param_grid(param_space: Dict[str, List]) -> List[Dict]:
    keys = param_space.keys()
    values = param_space.values()
    return [dict(zip(keys, combination)) for combination in product(*values)]
