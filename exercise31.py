def highest_value(a,b):
    # Write your solution
    if sum(map(ord,list(a))) > sum(map(ord,list(b))):
        return a
    elif sum(map(ord,list(a))) < sum(map(ord,list(b))):
        return b
    else:
        return a

print(highest_value("AaBbCcXxYyZz0189", "KkLlMmNnOoPp4567"))

def highest_value(a, b):
    return max(a, b, key=lambda s: sum(map(ord, s)))