from enum import IntEnum
from typing import List, NamedTuple
import math
from typing import Any
from collections import Counter
from typing import NamedTuple
from typing import Dict, TypeVar
from collections import defaultdict
T = TypeVar('T')


class QuestionEnum(IntEnum):
    LVL = 0
    LANG = 1
    DEGREE = 2
    OS = 3
    HIRE = 4
    DECLINE = 5


class Vacantion(NamedTuple):
    level: str
    lang: str
    degree: str
    OS: str


class Candidate:
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
        Vacantion('junior', 'python',   'yes',  'macos'),
        Vacantion('junior', 'python',   'no',   'macos'),
        Vacantion('junior', 'python',   'yes',  'windows'),
        Vacantion('junior', 'python',   'yes',  'linux'),
        Vacantion('senior', 'python',   'yes',  'windows'),
        Vacantion('senior', 'python',   'no',   'windows'),
        Vacantion('junior', 'c++',      'yes',  'windows'),
        Vacantion('junior', 'c++',      'yes',  'linux'),
        Vacantion('junior', 'c++',      'yes',  'macos'),
        Vacantion('middle', 'c++',      'yes',  'windows'),
        Vacantion('middle', 'c++',      'no',   'windows'),
        Vacantion('senior', 'c++',      'yes',  'windows'),
        Vacantion('senior', 'c++',      'yes',  'linux'),
        Vacantion('senior', 'c++',      'yes',  'macos'),
        Vacantion('senior', 'c++',      'no',   'windows'),
        Vacantion('senior', 'c++',      'no',   'linux'),
        Vacantion('senior', 'c++',      'no',   'macos'),
        Vacantion('junior', 'java',     'yes',  'linux'),
        Vacantion('junior', 'java',     'no',   'linux'),
        Vacantion('senior', 'java',     'yes',  'windows'),
        Vacantion('senior', 'java',     'no',   'windows'),
        Vacantion('junior', 'r',        'yes',  'macos'),
        Vacantion('middle', 'r',        'yes',  'linux'),
        Vacantion('middle', 'r',        'no',   'linux')
]


def find_min_entropy(data, attributes: List[str]) -> (QuestionEnum, float):
    values = [data_entropy_by(data, attr) for attr in attributes]
    attr_str = attributes[values.index(min(values))]
    if attr_str == 'level':
        attr = QuestionEnum.LVL
    if attr_str == 'lang':
        attr = QuestionEnum.LANG
    if attr_str == 'degree':
        attr = QuestionEnum.DEGREE
    if attr_str == 'OS':
        attr = QuestionEnum.OS
    return attr, min(values)


data = inputs.copy()


def find_attributes(c: Candidate) -> []:
    # верните массив тех аттрибутов кандидата, которые равны None
    res = []
    if c.level is None:
        res.append('level')
    if c.lang is None:
        res.append('lang')
    if c.degree is None:
        res.append('degree')
    if c.OS is None:
        res.append('OS')
    return res


def split_by(inputs: List[Vacantion], c: Candidate) -> list:
    data = inputs.copy()
    if c.level is not None:
        data = split(data, 'level', c.get_by('level'))
    if c.lang is not None:
        data = split(data, 'lang', c.get_by('lang'))
    if c.degree is not None:
        data = split(data, 'degree', c.get_by('degree'))
    if c.OS is not None:
        data = split(data, 'OS', c.get_by('OS'))
    return data


def split(data, attr: str, value: Any) -> list:
    if attr == 'level':
        return [candidate for candidate in data if candidate.level == value]
    if attr == 'lang':
        return [candidate for candidate in data if candidate.lang == value]
    if attr == 'degree':
        return [candidate for candidate in data if candidate.degree == value]
    if attr == 'OS':
        return [candidate for candidate in data if candidate.OS == value]



def select(c: Candidate) -> QuestionEnum:
    data = split_by(inputs, c)
    if len(data) == 0:
        return QuestionEnum.DECLINE

    attributes = find_attributes(c)
    if len(data) != 0 and len(attributes) == 0:
        return QuestionEnum.HIRE

    attr, value = find_min_entropy(data, attributes)
    return attr


