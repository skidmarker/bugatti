import math
from itertools import permutations


def solution(numbers):
    answer = 0
    nums = []
    for i in range(len(numbers)):
        nums += list(map(lambda x: int("".join(x)), permutations(numbers, i + 1)))
    nums = list(set(nums))

    def ckPrime(num):
        if num <= 1:
            return False

        for n in range(2, int(math.sqrt(num)) + 1):
            if num % n == 0:
                return False
        return True

    return len([v for v in nums if ckPrime(v)])
