from collections import deque


def solution(priorities, location):
    answer = 0
    q = deque()
    pr_dict = {}

    for i in range(len(priorities)):
        val = priorities[i]
        q.append((val, i))
        if val not in pr_dict:
            pr_dict[val] = 1
        else:
            pr_dict[val] += 1

    while len(q) > 0:
        pr, idx = q.popleft()
        if max(pr_dict.keys()) > pr:
            q.append((pr, idx))
        else:
            answer += 1
            if location == idx:
                break
            if pr_dict[pr] > 1:
                pr_dict[pr] -= 1
            else:
                del pr_dict[pr]

    return answer
