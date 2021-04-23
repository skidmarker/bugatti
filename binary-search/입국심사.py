def solution(n, times):
    times.sort()
    low, high = 1, times[-1] * n
    answer = high
    
    while high >= low:
        cur, people = (high + low) // 2, 0
        for t in times:
            people += cur // t
        if people < n:
            low = cur + 1 
        else:
            answer = min(answer, cur)
            high = cur - 1
    return answer
