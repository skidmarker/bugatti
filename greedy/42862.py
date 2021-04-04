def solution(n, lost, reserve):
    answer = n - len(lost)
    lost.sort()
    reserve.sort()
    ck = []

    for r in reserve:
        if r in lost:
            answer += 1
            lost.remove(r)
        else:
            ck.append(r)

    for r in ck:
        if r - 1 in lost:
            answer += 1
            lost.remove(r - 1)
        elif r + 1 in lost:
            answer += 1
            lost.remove(r + 1)

    return answer
