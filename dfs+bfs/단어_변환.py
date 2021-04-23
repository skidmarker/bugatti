from collections import deque


def get_diff_count(word1, word2):
    diff = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff += 1
    return diff


def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append((begin, 0))
    visited = [False] * len(words)

    while len(q) > 0:
        cur, cnt = q.popleft()
        if cur == target:
            answer = cnt
            break
        for i in range(len(words)):
            if not visited[i] and get_diff_count(cur, words[i]) == 1:
                visited[i] = True
                q.append((words[i], cnt + 1))
    return answer
