def solution(brown, yellow):
    answer = []
    sum_wh = (brown - 4) // 2
    mul_wh = yellow

    yw = sum_wh - 1
    yh = 1
    while yw >= yh:
        if yw * yh == mul_wh:
            answer = [yw + 2, yh + 2]
            break
        yw -= 1
        yh += 1

    return answer
