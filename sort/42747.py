def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    h, i = citations[0], 0
    while h >= 0 and i < len(citations):
        while citations[i] >= h:
            i += 1
            if len(citations) == i:
                answer = h if i >= h else i
                break
        if i >= h:
            answer = h
            break
        h -= 1
    return answer
