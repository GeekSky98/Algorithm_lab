from collections import deque

def bfs(computers, visited, start):
    queue = deque([start])
    while queue:
        s = queue.popleft()
        for i in range(len(computers)):
            if computers[s][i] == 1 and not visited[i]:
                visited[i] = True
                queue.append(i)

def solution(n, computers):
    visited = [False] * n
    answer = 0
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            bfs(computers, visited, i)
            answer += 1

    return answer