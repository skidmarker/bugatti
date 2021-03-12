def solution(array, commands):
    answer = []
    for i, j, k in commands:
        narr = sorted(array[i - 1 : j])
        if len(narr) >= k:
            answer.append(narr[k - 1])
        else:
            answer.append(narr[-k])
    return answer
