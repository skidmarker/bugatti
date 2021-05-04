def solution(triangle):
    answer = 0
    n = len(triangle)
    d = [[0] * n for _ in range(n)]
    d[0][0] = triangle[0][0]
    for i in range(n):
        for j in range(len(triangle[i])):
            d[i][j] = max(d[i - 1][j], d[i - 1][j - 1]) + triangle[i][j]
    answer = max(d[-1])
    return answer
