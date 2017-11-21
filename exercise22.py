from collections import Counter


def combine(oA, oB = {}, oC = {}, oD = {}, oE = {}, oF = {} ):
    return dict(Counter(oA) + Counter(oB) + Counter(oC) + Counter(oD) + Counter(oE) + Counter(oF))

def combine2(*bs):
    c = {}
    for b in bs:
        for k, v in b.items():
            c[k] = v + c.get(k, 0)
    return c


def combine3(*args):
    return sum((Counter(a) for a in args), Counter())


objA = {'a': 10, 'b': 20, 'c': 30}
objB = {'a': 3, 'c': 6, 'd': 3}
objC = { 'a': 5, 'd': 11, 'e': 8 }

#print(combine(objA, objB))
print(combine(objA, objC))

