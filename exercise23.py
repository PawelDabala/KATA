# from collections import Counter
# z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
# print(dict(Counter(z)))

#rozwiazanie z strony
from collections import Counter


class List(object):
    @staticmethod
    def count_spec_digits(integers_list, digits_list):
        counts = Counter(''.join(str(abs(a)) for a in integers_list))
        return [(b, counts[str(b)]) for b in digits_list]

class List2(object):
    def count_spec_digits(self, integers_list, digits_list):
        # your code here
        self.integers_list = integers_list
        self.digits_list = digits_list

        b_list = []
        str_list = "".join(str(self.integers_list))

        for i in self.digits_list:

            b_list.append((i, str_list.count(str(i))))


        return b_list



integers_list = [-18, -31, 81, -19, 111, -888]
digits_list = [1, 8, 4]

li = List2()
print(li.count_spec_digits(integers_list, digits_list))


