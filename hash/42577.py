def solution(phone_book):
    answer = True
    phone_book.sort()
    p_dict = {}
    for pn in phone_book:
        for i in range(1, len(pn)):
            if pn[:i] in p_dict:
                answer = False
                break
        p_dict[pn] = 1
    return answer
