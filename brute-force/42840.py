def solution(answers):
    answer = []
    n = len(answers)
    str_ans = "".join(list(map(str, answers)))

    def ckMatch(answer, submit):
        res = 0
        for i in range(len(answer)):
            if answer[i] == submit[i]:
                res += 1
        return res

    a, b, c = "12345", "21232425", "3311224455"
    a = a * (n // len(a)) + a[: n % len(a)]
    b = b * (n // len(b)) + b[: n % len(b)]
    c = c * (n // len(c)) + c[: n % len(c)]

    test = [ckMatch(str_ans, a), ckMatch(str_ans, b), ckMatch(str_ans, c)]
    if len(set(test)) == len(test):
        answer = [i + 1 for i in range(3) if max(test) == test[i]]
    else:
        answer = sorted(
            [(i + 1, test[i]) for i in range(3) if max(test) == test[i]],
            key=lambda x: (-x[1], x[0]),
        )
        answer = list(map(lambda x: x[0], answer))
    return answer
