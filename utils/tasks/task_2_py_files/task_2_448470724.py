from math import log2
from typing import List


def entropy(class_probabilities: List[float]) -> float:
    sum = 0
    for p in class_probabilities:
        if p != 0:
            sum += p * log2(p)
    return -sum