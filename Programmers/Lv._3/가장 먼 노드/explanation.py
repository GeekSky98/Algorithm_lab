from collections import deque, defaultdict
def solution(n, edge):
    graph = defaultdict(list)
    for x, y in edge:  # 양방향 그래프
        graph[x].append(y)
        graph[y].append(x)

    visited = [-1] * n
    visited[0] = 0
    queue = deque([1])

    while queue:
        now = queue.popleft()
        for next in graph[now]:
            if visited[next-1] == -1:
                visited[next-1] = visited[now-1] + 1
                queue.append(next)

    max_node = max(visited)
    return visited.count(max_node)