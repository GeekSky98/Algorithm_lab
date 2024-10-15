from collections import deque

def solution(n, computers):
    visited = [False] * n
    answer = 0
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            queue = deque([i])

            while queue:
                current = queue.popleft()

                for j in range(n):
                    if not visited[j] and computers[current][j]:
                        visited[j] = True
                        queue.append(j)
            answer += 1
    return answer

solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]])