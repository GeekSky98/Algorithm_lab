import sys
from collections import defaultdict
sys.setrecursionlimit(5000)

n, m = map(int, sys.stdin.readline().split())
father = list(sys.stdin.readline().strip())
line = [tuple(sys.stdin.readline().split()) for _ in range(n-1)]

graph_dic = defaultdict(list)
for s, e, a in line:
    graph_dic[int(s)].append((int(e), a))
    graph_dic[int(e)].append((int(s), a))

def cal_lcs(x, y):
    x_len, y_len = len(x), len(y)
    dp = [[0]*(y_len+1) for _ in range(x_len+1)]
    for i in range(1, x_len + 1):
        for j in range(1, y_len + 1):
            if x[i-1] == y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]

route_list = []
def dfs(node, parent_node, path):
    leaf_flag = True
    for next_node, next_char in graph_dic[node]:
        if next_node != parent_node:
            leaf_flag = False
            dfs(next_node, node, path + next_char)
    if leaf_flag:
        route_list.append(path)

dfs(1, -1, "")

answer = 0
for r in route_list:
    if len(r) > answer:
        num = cal_lcs(r, father)
        answer = max(answer, num)

print(answer)