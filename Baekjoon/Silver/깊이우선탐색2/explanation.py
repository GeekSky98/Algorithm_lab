import sys
from collections import defaultdict
n, m, r = map(int, sys.stdin.readline().split())
node_list = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

def solution(n, m, r, node_list):
    answer = [0] * (n+1)
    graph = defaultdict(list)

    for node, next in node_list:
        graph[node].append(next)
        graph[next].append(node)

    stack = [r]
    cnt = 1
    while stack:
        node = stack.pop()
        if answer[node] == 0:
            answer[node] = cnt
            cnt += 1
            for next_node in sorted(graph[node]):
                if answer[next_node] == 0:
                    stack.append(next_node)

    for i in range(1, n+1):
        print(answer[i])

solution(n, m, r, node_list)