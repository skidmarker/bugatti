def solution(price, money, count):
    answer = -1
    total = price * ((count * (count + 1)) // 2)
    answer = 0 if money - total >= 0 else total - money
    return answer
