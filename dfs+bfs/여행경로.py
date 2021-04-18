finish = False
use = 0


def solution(tickets):
    answer = []
    visited = [False] * len(tickets)
    tickets.sort()

    def dfs(cur):
        global finish
        global use
        if use == len(tickets):
            finish = True
            return
        for i in range(len(tickets)):
            if tickets[i][0] == cur and not visited[i]:
                visited[i] = True
                answer.append(tickets[i][1])
                use += 1
                dfs(tickets[i][1])
                if not finish:
                    visited[i] = False
                    use -= 1
                    answer.pop()

    answer.append("ICN")
    dfs("ICN")
    return answer
