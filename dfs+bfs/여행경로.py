finish = False


def solution(tickets):
    answer = []
    visited = []
    tickets.sort()

    def dfs(cur, finish):
        if len(visited) == len(tickets):
            finish = True
            return
        for id in range(len(tickets)):
            if tickets[id][0] == cur and not (id in visited):
                visited.append(id)
                answer.append(tickets[id][1])
                dfs(tickets[id][1], finish)
                if finish == False:
                    visited.remove(id)
                    answer.remove(tickets[id][1])
                print(answer)

    answer.append("ICN")
    dfs("ICN", False)
    return answer
