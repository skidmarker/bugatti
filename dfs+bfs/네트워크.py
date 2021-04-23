# 컴포넌트 개수 세는 문제
def solution(n, computers):
    answer = 0
    visited = [False] * (n + 1)

    def dfs(s):
        visited[s] = True
        for i in range(len(computers[s])):
            if i != s and computers[s][i] == 1 and not visited[i]:
                dfs(i)

    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    return answer
