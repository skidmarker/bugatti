N = int(input())
lines = [list(map(int, input().split())) for _ in range(N)]
cur, total = list(lines[0]), 0

for s, e in lines[1:]:
    if s <= cur[1] and e > cur[1]:
        cur[1] = e
    if s > cur[1]:
        total += cur[1] - cur[0]
        cur = [s, e]
total += cur[1] - cur[0]
print(total)
