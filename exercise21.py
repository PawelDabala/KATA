def pipe_fix(list1):
    return [ x for x in range(list1[0],list1[-1]+1)]

# print(pipe_fix([1,4,6]))

def pipe_fix2(nums):
    return range(nums[0], nums[-1] + 1)

print(pipe_fix2([1,4,6]))