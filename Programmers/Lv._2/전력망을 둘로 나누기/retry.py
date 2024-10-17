from collections import defaultdict

def solution(n, wires):
    graph = defaultdict(list)
    for s, e in wires:
        graph[s].append(e)
        graph[e].append(s)

    visited = [False] * (n + 1)

    def dfs(start, cut_node):
        cost = 1
        visited[start] = True

        for next_node in graph[start]:
            if next_node != cut_node and not visited[next_node]:
                cost += dfs(next_node, cut_node)

        visited[start] = False
        return cost

    answer = float('inf')
    for s, e in wires:
        cost = dfs(s, e)
        answer = min(answer, abs((n - cost) - cost))

    return answer