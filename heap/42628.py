import heapq


def heapsort(arr, reverse=False):
    pq, res = [], []
    if reverse:
        for num in arr:
            heapq.heappush(pq, -num)
        heapq.heappop(pq)
        while len(pq) > 0:
            res += [-heapq.heappop(pq)]
    else:
        for num in arr:
            heapq.heappush(pq, num)
        heapq.heappop(pq)
        while len(pq) > 0:
            res += [heapq.heappop(pq)]
    return res


def solution(operations):
    answer = [0, 0]
    q = []
    for operation in operations:
        op, num = operation.split()
        num = int(num)
        if op == "I":
            q.append(num)
            if num > answer[0] or len(q) == 1:
                answer[0] = num
            if num < answer[1] or len(q) == 1:
                answer[1] = num
        else:
            if len(q) == 0:
                continue
            if num == 1:
                q = heapsort(q, reverse=True)
                if len(q) > 0:
                    answer[0] = q[0]
                else:
                    answer = [0, 0]
            else:
                q = heapsort(q)
                if len(q) > 0:
                    answer[1] = q[0]
                else:
                    answer = [0, 0]
    return answer
