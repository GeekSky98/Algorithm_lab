import sys
from collections import defaultdict, deque

node, line = map(int, sys.stdin.readline().split())
graph_line = [list(map(int, sys.stdin.readline().split())) for _ in range(line)]
start, end = map(int, sys.stdin.readline().split())

graph_dic = defaultdict(list)
for s, e in graph_line:
    graph_dic[s].append(e)

def detect(st, graph, no):
    temp_set = set()
    queue = deque([st])
    temp_set.add(st)

    while queue:
        now_node = queue.popleft()
        for next_node in graph[now_node]:
            if next_node != no and next_node not in temp_set:
                queue.append(next_node)
                temp_set.add(next_node)

    return temp_set

start_set = detect(start, graph_dic, end)
end_set = detect(end, graph_dic, start)

print(len(start_set & end_set))