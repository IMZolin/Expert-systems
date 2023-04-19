from task_3_448470724 import data_entropy
from typing import List
import math
from typing import Any
from collections import Counter
import random

# from main import data_entropy


def fff(labels: List[Any]) -> List[float]:
    total_count = len(labels)
    res = []
    for count in Counter(labels).values():
        res.append(count / total_count)
    return res


def ffff(class_probabilities: List[float]) -> float:
    return sum(-p * math.log(p, 2) for p in class_probabilities if p > 0)


def ff(labels: List[Any]) -> float:
    return ffff(fff(labels))


def main():
    result = 0
    test1 = [random.randint(0, 10) for i in range(10)]
    if data_entropy(test1) == ff(test1):
        result = 1

    print(result)


if __name__ == '__main__':
    main()