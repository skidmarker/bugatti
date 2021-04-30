from collections import deque


def bfs(start, n, adj):
    q = deque()
    visited = [False] * (n + 1)
    mx, cnt = 0, 0
    q.append((start, 0))
    visited[start] = True
    while len(q) > 0:
        cur, d = q.popleft()
        if d > mx:
            cnt = 1
            mx = d
        elif d == mx:
            cnt += 1
        for n in adj[cur]:
            if not visited[n]:
                q.append((n, d + 1))
                visited[n] = True
    return cnt


def solution(n, edge):
    adj = [[] for _ in range(n + 1)]
    for u, v in edge:
        adj[u].append(v)
        adj[v].append(u)

    return bfs(1, n, adj)
