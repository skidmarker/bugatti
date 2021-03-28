import heapq


def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)
    while len(scoville) > 0:
        if scoville[0] >= K:
            return answer
        if len(scoville) < 2:
            break
        answer += 1
        f = heapq.heappop(scoville)
        s = heapq.heappop(scoville)
        nxt = f + s * 2
        heapq.heappush(scoville, nxt)
    return -1
