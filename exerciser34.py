# Two numbers are relatively prime if their greatest common factor is 1.
# In other worst if they cannot be divided by any common numbers other than 1, they are relatively prime.
# 13, 16, 9, 5, an 119 are all relatively prime because there share no common factors except for 1, to easily see this I will show their factorizations,
# 13, 2 x 2 x 2 x 2, 3 x 3, 5, 17 x 7
#
# Create a function that takes 2 inputs, an number, n and a list, l.
# The function should return a list of all the numbers in l that are relatively prime to n.
# n and all numbers in l will be positive integers greater than or equal to 0.

def relatively_prime (n,l):
    primes = []
    final_primes = []

    for num in range(1, n):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)

    for i in l:
        is_prime = True
        for j in primes:
            if i % j == 0:
                is_prime =False
        if is_prime:
            final_primes.append(i)

    return  final_primes

print(relatively_prime(8,[1,2,3,4,5,6,7]))



from fractions import gcd
def relatively_prime2 (n, l):
    return [x for x in l if gcd(n, x) == 1]
