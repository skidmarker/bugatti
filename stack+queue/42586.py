from collections import deque


def solution(progresses, speeds):
    answer = []
    days = deque()
    for i in range(len(progresses)):
        day = ((100 - progresses[i]) // speeds[i]) + (
            (100 - progresses[i]) % speeds[i] != 0
        )
        days.append(day)

    prev, cnt = days[0], 0
    while len(days) > 0:
        d = days.popleft()
        if prev < d:
            answer.append(cnt)
            cnt = 1
            prev = d
        else:
            cnt += 1
        if len(days) == 0:
            answer.append(cnt)
    return answer
