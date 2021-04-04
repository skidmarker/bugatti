import heapq


def solution(routes):
    answer = 0
    routes.sort()
    pq = []
    for s, e in routes:
        if len(pq) == 0:
            heapq.heappush(pq, (-e, (s, e)))
        else:
            pf, route = pq[0]
            if route[1] >= s and route[1] > e:
                heapq.heappop(pq)
                heapq.heappush(pq, (-e, (route[0], e)))
            elif s > route[1]:
                heapq.heappush(pq, (-e, (s, e)))
    answer = len(pq)
    return answer
