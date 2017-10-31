"""
Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.
"""
def add_binary(a,b):
    return '{0:b}'.format(a+b)


print(add_binary(2,4))

#Best Practices
def add_binary2(a,b):
    return bin(a+b)[2:]

print(add_binary2(2,4))