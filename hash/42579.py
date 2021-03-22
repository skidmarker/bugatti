def solution(genres, plays):
    answer = []
    s_dict, cnt_dict, n = {}, {}, len(genres)
    for i in range(n):
        g, p = genres[i], plays[i]
        if g not in s_dict:
            s_dict[g] = [(-p, i)]
            cnt_dict[g] = p
        else:
            s_dict[g].append((-p, i))
            cnt_dict[g] += p

    for k, v in sorted(cnt_dict.items(), key=lambda x: x[1], reverse=True):
        s_dict[k].sort()
        if len(s_dict[k]) == 1:
            answer.append(s_dict[k][0][1])
        else:
            for i in range(2):
                answer.append(s_dict[k][i][1])
    return answer
