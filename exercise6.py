"""
Given an array of one's and zero's convert the equivalent binary value to an integer.

Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1

"""

def binary_array_to_number(arr):
    return int(''.join(list(map(str,arr))),2)



print(binary_array_to_number([0, 1, 0, 1]))
