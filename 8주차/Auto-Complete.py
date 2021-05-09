W, N = map(int, input().split())
words = [input() for _ in range(W)]
inputs = [input().split() for _ in range(N)]
cache = {chr(ord("a") + key): [] for key in range(26)}

for idx, word in enumerate(words):
    words[idx] = (word, idx + 1)
for word, idx in sorted(words, key=lambda x: x[0]):
    cache[word[0]].append((word, idx))
# print(cache)

for i, cur in inputs:
    cur_dict = []
    for word, idx in cache[cur[0]]:
        if len(word) >= len(cur) and word[: len(cur)] == cur:
            cur_dict += [(word, idx)]
    if len(cur_dict) >= int(i):
        print(cur_dict[int(i) - 1][1])
    else:
        print(-1)
