import sys
from collections import defaultdict, deque

n, q = map(int, sys.stdin.readline().split())
rel = [list(map(int, sys.stdin.readline().split())) for _ in range(n-1)]
qa = [list(map(int, sys.stdin.readline().split())) for _ in range(q)]

def bfs(start, end, graph):
    queue = deque([(start, 0)])
    visited = [False] * (len(graph) + 1)
    visited[start] = True

    while queue:
        now, cost = queue.popleft()
        if now == end:
            return cost

        for next_node, next_cost in graph[now]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append((next_node, cost + next_cost))

def solution(rela, ques):
    graph = defaultdict(list)
    for a, b, c in rela:
        graph[a].append((b, c))
        graph[b].append((a, c))

    for q, a in ques:
        print(bfs(q, a, graph))

solution(rel, qa)