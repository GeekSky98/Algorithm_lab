def solution(k, dungeons):
    dungeons_len = len(dungeons)
    visited = [False] * dungeons_len

    def dfs(stemina, d_cnt):
        max_cnt = d_cnt

        for i in range(dungeons_len):
            if not visited[i] and stemina >= dungeons[i][0]:
                visited[i] = True
                max_cnt = max(max_cnt, dfs(stemina - dungeons[i][1], d_cnt + 1))
                visited[i] = False

        return max_cnt

    return dfs(k, 0)