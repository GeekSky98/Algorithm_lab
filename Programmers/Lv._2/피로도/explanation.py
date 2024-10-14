def solution(k, dungeons):
    answer = -1
    d_len = len(dungeons)
    visited = [False] * d_len

    def dfs(stemina, count):
        current = count

        for i in range(d_len):
            if not visited[i]:
                if dungeons[i][0] <= stemina:
                    visited[i] = True
                    current = max(current, dfs(stemina - dungeons[i][1], count + 1))
                    visited[i] = False

        return current

    return dfs(k, 0)