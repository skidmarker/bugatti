N = int(input())
startline = [input() for _ in range(N)]
endline = [input() for _ in range(N)]

wait = set()

for i in range(len(startline)):
    if startline[i] in wait:
        continue
    while len(endline) > 0:
        cur = endline.pop(0)
        if startline[i] == cur:
            break
        else:
            wait.add(cur)
print(len(wait))
