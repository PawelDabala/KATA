# My washing machine uses W amount of water to wash C amount of clothes. For every 1 unit increase in clothes, the washing machine will use 10% more water (multiplicative) to clean (i.e. For C = C + 1, W = W * 110%.
#
# Write a function howMuchWater (JS)/how_much_water (Python) to work out how much water is needed if you have a C amount of clothes. The function will accept 3 parameters - howMuchWater(W,L,C) / how_much_water(W,L,C)
#
# My washing machine is an old model that can only handle double the amount of L. If C > 2L, return 'Too much clothes'. The washing machine also cannot handle any amount of clothes less than L. If that is the case, return 'Not enough clothes'.
#
# The answer should be rounded to the nearest 2 decimal places.
def how_much_water(W,L,C):
    if C > 2 * L:
        return 'Too much clothes'
    elif C < L:
        return 'Not enough clothes'

    for i in range(C-L):
        W *= 1.10
    return round(W,2)

print(how_much_water(10,11,20))

