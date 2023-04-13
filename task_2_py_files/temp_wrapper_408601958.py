from task_2_py_files.task_2_408601958 import entropy
import math
from math import log2
import random
from typing import List


def fff(class_probabilities: List[float]) -> float:
    return sum(-p * math.log(p, 2) for p in class_probabilities if p > 0)


def main():
    result = 0
    test1 = [random.randint(0, 10)/10 for i in range(10)]
    if entropy(test1) == fff(test1):
        result = 1

    print(result)


if __name__ == '__main__':
    main()