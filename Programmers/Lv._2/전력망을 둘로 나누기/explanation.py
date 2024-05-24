from collections import defaultdict
def solution(n, wires):
    answer = []
    graph = defaultdict(list)

    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    visited = [False] * (n + 1)

    def dfs(g, v, start, end):
        cnt = 1
        v[start] = True
        for next_node in g[start]:
            if next_node == end or v[next_node]:
                continue
            cnt += dfs(g, v, next_node, end)
        v[start] = False
        return cnt

    for node, line in wires:
        left_cnt = dfs(graph, visited, node, line)
        answer.append(abs(left_cnt - (n - left_cnt)))

    return min(answer)