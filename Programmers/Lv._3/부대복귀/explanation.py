from collections import defaultdict, deque

def bfs(n, s, destination, graph):
    visited = [False] * (n+1)
    visited[s] = True
    queue = deque([(s, 0)])

    while queue:
        node, cost = queue.popleft()

        if node == destination:
            return cost

        for next_node in graph[node]:
            if not visited[next_node]:
                queue.append((next_node, cost + 1))
                visited[next_node] = True

    return -1


def solution(n, roads, sources, destination):
    graph = defaultdict(list)
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    answer = []
    for s in sources:
        answer.append(bfs(n, s, destination, graph))

    return answer

# ------ 성능 상 반대로 하는게 이득.

from collections import defaultdict, deque

def bfs(n, s, graph):
    dist = [-1] * (n+1)
    dist[s] = 0
    queue = deque([(s, 0)])

    while queue:
        node, cost = queue.popleft()

        for next_node in graph[node]:
            if dist[next_node] == -1:
                queue.append((next_node, cost + 1))
                dist[next_node] = cost + 1

    return dist


def solution(n, roads, sources, destination):
    graph = defaultdict(list)
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    dist = bfs(n, destination, graph)
    answer = []

    for s in sources:
        answer.append(dist[s])

    return answer