N = int(input())
keys = [input() for _ in range(N)]

shortcut = {}
result = []

for key in keys:
    flag = False
    cur = key.split()
    for i, word in enumerate(cur):
        if not word[0].lower() in shortcut:
            shortcut[word[0].lower()] = key
            cur[i] = "[" + word[0] + "]" + word[1:]
            flag = True
            break
        if flag:
            break

    if not flag:
        for i, word in enumerate(cur):
            for j in range(1, len(word)):
                if not word[j].lower() in shortcut:
                    shortcut[word[j].lower()] = key
                    cur[i] = (
                        word[:j] + "[" + word[j] + "]" + word[j + 1 :]
                        if j < len(word) - 1
                        else word[:j] + "[" + word[j] + "]"
                    )
                    flag = True
                    break
            if flag:
                break
    result.append(" ".join(cur))
print(*result, sep="\n")
