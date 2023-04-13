from typing import List
import math
from typing import Any
from collections import Counter


def entropy(class_probabilities: List[float]) -> float:
    return sum(-p * math.log(p, 2) for p in class_probabilities if p > 0)


def class_probabilities(labels: List[Any]) -> List[float]:
    total_count = len(labels)
    res = []
    for count in Counter(labels).values():
        res.append(count / total_count)
    return res


def data_entropy(labels: List[Any]) -> float:
    return entropy(class_probabilities(labels))