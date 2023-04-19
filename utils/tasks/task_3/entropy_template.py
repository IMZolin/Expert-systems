from collections import Counter
from math import log2


# here you need to write the function counts probabilities of each label
def class_probabilities(labels: list[str]) -> list[float]:
    # tip: you can use class Counter to count a number of label in collection(in our case collection is list)
    #                           ^ check documentation
    pass


# here you need to write the function counts an entropy of labels
# this function receives the list of probabilities you counted in previous function
def entropy(probabilities: list[float]) -> float:
    pass


# you need to define labels with given data
if __name__ == '__main__':
    labels = []
    print(entropy(class_probabilities(labels)))
