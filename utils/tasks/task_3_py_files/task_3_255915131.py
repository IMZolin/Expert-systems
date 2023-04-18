from typing import List
import math
from typing import Any
from collections import Counter


def entropy(class_probabilities: List[float]) -> float:
    return sum(-p * math.log(p, 2) for p in class_probabilities if p > 0)


def class_probabilities(labels: List[Any]) -> List[float]:
    """
        Реализуйте здесь преобразование, которое изложено на слайде,
        для подсчета числа вхождений элемента в множество можно использовать:

        for count in Counter(labels).values():
            ...
    """
    a = List[float]
    for count in Counter(labels).values():
        a.append(count / len(labels))
    return a


def data_entropy(labels: List[Any]) -> float:
    return entropy(class_probabilities(labels))
