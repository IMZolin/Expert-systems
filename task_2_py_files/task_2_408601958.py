from math import log2
from typing import List


def entropy(class_probabilities: List[float]) -> float:
    return sum(-p*log2(p) for p in class_probabilities if p > 0)