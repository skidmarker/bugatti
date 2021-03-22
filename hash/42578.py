def solution(clothes):
    answer = 1
    c_dict = {}
    for c, type in clothes:
        if type in c_dict:
            c_dict[type] += 1
        else:
            c_dict[type] = 1

    for cnt in c_dict.values():
        answer *= cnt + 1

    return answer - 1
