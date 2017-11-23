def is_opposite(s1,s2):

    if s1 == "" or s2 == "":
        return False

    list_1 = [ i.islower() for i in s1 ]
    list_2 = [not i.islower() for i in s2]

    return list_1 == list_2

print(is_opposite("aBcd", "AbCD"))

def is_opposite2(s1, s2):
    return False if not(s1 or s2) else s1.swapcase() == s2