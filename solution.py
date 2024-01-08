"""
Amicable Numbers
"""
import math


def factors(num):
    "Returns sum of all factors (except num) of num"
    factor = [i for i in range(1, round(math.sqrt(num) + 1)) if num % i == 0]
    mirror = [int(num / i) for i in range(1, round(math.sqrt(num) + 1)) if num % i == 0]
    if factor:
        allf = factor + mirror
        allf.remove(num)
        if len(allf) > 1:
            return sum(allf)
    return None


def answer():
    """Returns the sum of all the amicable numbers under 10000"""
    return solver(1, 10000)


def solver(p: int, q: int):
    """Returns the sum of all the amicable numbers between range p and q"""
    ami = []
    for i in range(p, q):
        if factors(i) and i != factors(i) and i == factors(factors(i)) and i not in ami:
            ami.append(i)
            ami.append(factors(i))
    return sum(ami)
