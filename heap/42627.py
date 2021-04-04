import heapq


def solution(jobs):
    answer = 0
    jobs.sort()
    pq, cur, time = [], 0, 0
    for i in range(len(jobs), 0, -1):
        # 가장 처음에 시작하는 작업이 현재 시간보다 크면, 시작시간 재설정
        if len(pq) == 0 and jobs[cur][0] > time:
            time = jobs[cur][0]
        for j in range(cur, len(jobs)):
            if len(pq) >= i:
                break
            # 현재 시간 기준 이하의 모든 작업을 jobs에 넣기(= 현재 시점에서 실행할 수 있는 모든 작업들)
            if jobs[j][0] <= time:
                heapq.heappush(pq, ((jobs[j][1], jobs[j][0]), jobs[j]))
            else:
                cur = j
                break
        # pq에서 작업을 꺼내 1번의 작업을 매회마다 CPU에서 수행 => 비선점형 SJF 작업
        p, val = heapq.heappop(pq)
        time += val[1]
        answer += time - val[0]
    return answer // len(jobs)
