def main():
    r, c = map(int, input().split())
    ground = [input() for _ in range(r)]
    visited = [[False] * c for _ in range(r)]
    sheep, wolf = 0, 0

    def search_zone(x, y, r, c):
        o, v = 0, 0
        q = [(x, y)]
        while len(q) > 0:
            cx, cy = q.pop(0)
            if ground[cx][cy] == "o":
                o += 1
            elif ground[cx][cy] == "v":
                v += 1
            for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = cx + i, cy + j
                if nx >= 0 and nx < r and ny >= 0 and ny < c:
                    if not visited[nx][ny] and ground[nx][ny] != "#":
                        visited[nx][ny] = True
                        q.append((nx, ny))
        return (o, 0) if o > v else (0, v)

    for i in range(r):
        for j in range(c):
            if not visited[i][j] and ground[i][j] != "#":
                visited[i][j] = True
                o, v = search_zone(i, j, r, c)
                sheep += o
                wolf += v
    print(sheep, wolf)
