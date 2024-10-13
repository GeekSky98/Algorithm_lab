def solution(ability):
    student_len = len(ability)
    sport_len = len(ability[0])

    visited = [False] * student_len
    max_sum = 0

    def dfs(sport_idx, current_sum):
        nonlocal max_sum

        if sport_idx == sport_len:
            max_sum = max(max_sum, current_sum)
            return

        for i in range(student_len):
            if not visited[i]:
                visited[i] = True
                dfs(sport_idx + 1, current_sum + ability[i][sport_idx])
                visited[i] = False

    dfs(0, 0)

    return max_sum