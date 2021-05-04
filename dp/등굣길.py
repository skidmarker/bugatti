def solution(m, n, puddles):
    answer = 0
    dn = 1000000007
    matrix = [[0] * (m + 1) for _ in range(n + 1)]
    for x, y in puddles:
        matrix[y][x] = 1
    d = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if matrix[i][j] == 1:
                continue
            if i == 1 and j == 1:
                d[i][j] = 1
            else:
                d[i][j] = (d[i - 1][j] + d[i][j - 1]) % dn
    answer = d[n][m]
    return answer
