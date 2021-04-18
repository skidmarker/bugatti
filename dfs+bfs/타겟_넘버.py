def solution(numbers, target):
    answer = 0

    def dfs(cur, step, count):
        if step >= len(numbers):
            if cur == target:
                count += 1
            return count
        count = dfs(cur + numbers[step], step + 1, count)
        count = dfs(cur - numbers[step], step + 1, count)
        return count

    answer = dfs(numbers[0], 1, 0) + dfs(-numbers[0], 1, 0)
    return answer
