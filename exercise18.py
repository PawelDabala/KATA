"""
Count the number of occurencences of each character
and return it as a list of tuples in order of appearance.

"""
def ordered_count(input):
    list_later = []
    list_final = []
    for later in input:
        if later not in list_later:
            list_later.append(later)
            list_final.append((later, input.count(later)))

    return list_final

print(ordered_count("abracadabra"))


#rozwiazanie z strony
from collections import OrderedDict, Counter


class OrderedCounter(Counter, OrderedDict):
    pass


def ordered_count(seq):
    return list(OrderedCounter(seq).items())
