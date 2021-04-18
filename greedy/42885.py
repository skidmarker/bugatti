import heapq


def solution(people, limit):
    answer = 0
    boat = []
    people.sort(reverse=True)
    for p in people:
        if len(boat) == 0:
            heapq.heappush(boat, p)
        else:
            if boat[0] + p <= limit:
                heapq.heappop(boat)
                answer += 1
            else:
                heapq.heappush(boat, p)
    return len(boat) + answer
