# In this kata, your job is to return the two highest values in a list, this doesn't include duplicates.
#
# When given an empty list, you should also return an empty list, no strings will be passed into the list.
#
# The return should also be ordered from highest to lowest.
#
# If the argument passed isn't a list, you should return false.
#
# Examples:
#
# two_highest([4, 10, 10, 9]) should return [10, 9]
#
# two_highest([]) should return []
#
# two_highest("test") should return False

def two_highest(arg1):
    if isinstance(arg1, list):
        if len(arg1)> 0:
            maxs=[]
            maxs.append(max(arg1))
            arg1 = [ y for y in arg1 if y != max(arg1)]
            if len(arg1) > 0:
                maxs.append(max(arg1))
                return maxs
            else:
                return maxs
        else:
            return []
    else:
        return False

print(two_highest([15, 20, 20, 17]))
print(two_highest([]))

def two_highest2(ls):
    result = sorted(list(set(ls)), reverse=True)[:2]
    return result if isinstance(ls, (list)) else False