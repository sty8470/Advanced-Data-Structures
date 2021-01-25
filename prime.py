from math import *
def is_prime(n):
    n = int(n)
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def is_three_digits_sum_prime(n):
    for i in range (len(n)-2):
        seg = int(n[0]) + int(n[1]) + int(n[2])
        if is_prime(seg) == False:
            return False
    return True

print(is_three_digits_sum_prime('283002'))
