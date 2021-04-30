from collections import defaultdict


def solution(N, number):
    answer = -1
    if number == N:
        return 1

    cache = defaultdict(set)
    cache[1] = {N}
    for n in range(2, 9):
        for i in range(1, n):
            cache[n].add(int(str(N) * n))
            for n1 in cache[i]:
                for n2 in cache[n - i]:
                    cache[n].add(n1 + n2)
                    cache[n].add(n1 - n2)
                    cache[n].add(n1 * n2)
                    if n2 != 0:
                        cache[n].add(n1 // n2)
            if number in cache[n]:
                return n
    return answer
