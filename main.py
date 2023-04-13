from enum import IntEnum
from typing import List, Tuple
import math
from typing import Any
from collections import Counter, defaultdict
from typing import NamedTuple
from typing import Dict, TypeVar

T = TypeVar('T')

def entropy(class_probabilities: List[float]) -> float:
    """Given a list of class probabilities, compute the entropy"""
    return sum(-p * math.log(p, 2) for p in class_probabilities if p > 0)


def class_probabilities(labels: List[Any]) -> List[float]:
    total_count = len(labels)
    res = []
    for count in Counter(labels).values():
        res.append(count / total_count)
    return res


def data_entropy(labels: List[Any]) -> float:
    return entropy(class_probabilities(labels))


class QuestionEnum(IntEnum):
    LVL = 0
    LANG = 1
    DEGREE = 2
    OS = 3
    HIRE = 4
    DECLINE = 5


class Candidate(NamedTuple):
    level: str = None
    lang: str = None
    degree: str = None
    OS: str = None

    def get_by(self, attr: str) -> str:
        if attr == 'level':
            return self.level
        if attr == 'lang':
            return self.lang
        if attr == 'degree':
            return self.degree
        if attr == 'OS':
            return self.OS


def data_by(inputs: List[T], attribute: str) -> Dict[Any, List[T]]:
    """Partition the inputs into lists based on the specified attribute."""
    partitions: Dict[Any, List[T]] = defaultdict(list)
    for input in inputs:
        key = getattr(input, attribute)  # value of the specified attribute
        partitions[key].append(input)    # add input to the correct partition
    return partitions


def data_entropy_by(inputs: List[Any], attribute: str) -> float:
    """Compute the entropy corresponding to the given partition"""
    partitions = data_by(inputs, attribute)

    labels = []
    for partition in partitions.values():
        for input in partition:
            k = getattr(input, attribute)
            labels.append(k)

    return data_entropy(labels)


inputs = [
                #  level     lang        phd    o_system
        Candidate('junior', 'python',   'yes',  'macos'),
        Candidate('junior', 'python',   'no',   'macos'),
        Candidate('junior', 'python',   'yes',  'windows'),
        Candidate('junior', 'python',   'yes',  'linux'),
        Candidate('senior', 'python',   'yes',  'windows'),
        Candidate('senior', 'python',   'no',   'windows'),
        Candidate('junior', 'cpp',      'yes',  'windows'),
        Candidate('junior', 'cpp',      'yes',  'linux'),
        Candidate('junior', 'cpp',      'yes',  'macos'),
        Candidate('middle', 'cpp',      'yes',  'windows'),
        Candidate('middle', 'cpp',      'no',   'windows'),
        Candidate('senior', 'cpp',      'yes',  'windows'),
        Candidate('senior', 'cpp',      'yes',  'linux'),
        Candidate('senior', 'cpp',      'yes',  'macos'),
        Candidate('senior', 'cpp',      'no',   'windows'),
        Candidate('senior', 'cpp',      'no',   'linux'),
        Candidate('senior', 'cpp',      'no',   'macos'),
        Candidate('junior', 'java',     'yes',  'linux'),
        Candidate('junior', 'java',     'no',   'linux'),
        Candidate('senior', 'java',     'yes',  'windows'),
        Candidate('senior', 'java',     'no',   'windows'),
        Candidate('junior', 'r',        'yes',  'macos'),
        Candidate('middle', 'r',        'yes',  'linux'),
        Candidate('middle', 'r',        'no',   'linux')
]


def main():
    select(Candidate('senior', 'python', 'no', 'windows'))


def find_min_entropy(data, attributes: list) -> Tuple[str, float]:
    values = [data_entropy_by(data, attr) for attr in attributes]
    return attributes[values.index(min(values))], min(values)


def interpreter_answer(attr: str, value: str):
    if attr == 'level':
        return value
    if attr == 'lang':
        return value
    if attr == 'degree':
        if value == 'Yes' or value == 'yes' or value == 'y':
            return 'yes'
        else:
            return 'no'
    if attr == 'OS':
        return value


def split(data, attr: str, value: Any) -> list:
    answer = interpreter_answer(attr, value)
    if attr == 'level':
        return [candidate for candidate in data if candidate.level == answer]
    if attr == 'lang':
        return [candidate for candidate in data if candidate.lang == answer]
    if attr == 'degree':
        return [candidate for candidate in data if candidate.degree == answer]
    if attr == 'OS':
        return [candidate for candidate in data if candidate.OS == answer]


def ask_question(attr: str) -> str:
    if attr == 'level':
        return 'Какой у Вас уровень программирования?'
    if attr == 'lang':
        return 'Какой Ваш основной язык программирования?'
    if attr == 'degree':
        return 'Есть ли у вас высшее образование?'
    if attr == 'OS':
        return 'Какую операционную систему предпочитаете?'


def select(candidate: Candidate):
    attributes = ['level', 'lang', 'degree', 'OS']
    data = inputs.copy()


    values = [data_entropy_by(data, attr) for attr in attributes]
    for i in range(len(attributes)):
        print(attributes[i] + ' entropy = ' + str(values[i]))
    attr, min_val = find_min_entropy(data, attributes)
    print('min value:', attr, min_val)
    value = input(ask_question(attr) + '\n')
    attributes.remove(attr)
    data = split(data, attr, value)


    values = [data_entropy_by(data, attr) for attr in attributes]
    for i in range(len(attributes)):
        print(attributes[i] + ' entropy = ' + str(values[i]))
    attr, min_val = find_min_entropy(data, attributes)
    print('min value:', attr, min_val)
    value = input(ask_question(attr) + '\n')
    attributes.remove(attr)
    data = split(data, attr, value)


    values = [data_entropy_by(data, attr) for attr in attributes]
    for i in range(len(attributes)):
        print(attributes[i] + ' entropy = ' + str(values[i]))
    attr, min_val = find_min_entropy(data, attributes)
    print('min value:', attr, min_val)
    value = input(ask_question(attr) + '\n')
    attributes.remove(attr)
    data = split(data, attr, value)


    values = [data_entropy_by(data, attr) for attr in attributes]
    for i in range(len(attributes)):
        print(attributes[i] + ' entropy = ' + str(values[i]))
    attr, min_val = find_min_entropy(data, attributes)
    print('min value:', attr, min_val)
    value = input(ask_question(attr) + '\n')
    attributes.remove(attr)
    data = split(data, attr, value)


    values = [data_entropy_by(data, attr) for attr in attributes]
    for i in range(len(attributes)):
        print(attributes[i] + ' entropy = ' + str(values[i]))
    attr, min_val = find_min_entropy(data, attributes)
    print('min value:', attr, min_val)
    value = input(ask_question(attr) + '\n')
    attributes.remove(attr)
    data = split(data, attr, value)


if __name__ == '__main__':
    main()

