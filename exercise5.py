"""
uild Tower

Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *

Python: return a list;
"""
def tower_builder2(s):
    nr_ = s + (s- 1)
    lis_ = []
    str_ = '*' * nr_
    lis_.append(str_)

    for i in range(nr_ - 1, 1, -1):
        if (i - 1) % 2 != 0:
            str_ = ('*' * (i - 1))
            str_ = (' ' * (nr_ - len(str_) -1)) + str_ + (' ' * (nr_ - len(str_) -1))
            lis_.append(str_)
            nr_ -= 1

    return list(reversed(lis_))

print(tower_builder2(3))


def tower_builder2(n_floors):
    if n_floors == 0:
        return []

    count = 1
    result = []

    for i in range(1, n_floors + 1):
        stars = '*' * (2 * i - 1)
        space = ' ' * (n_floors - i)
        result.append(space + stars + space)

    return result





