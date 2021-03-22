def solution(participant, completion):
    answer = ""
    p_dict = {}

    for c in completion:
        if c in p_dict:
            p_dict[c] += 1
        else:
            p_dict[c] = 1

    for p in participant:
        if p not in p_dict or p_dict[p] == 0:
            answer = p
            break
        p_dict[p] -= 1

    return answer
