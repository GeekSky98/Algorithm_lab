import sys
from collections import defaultdict
sys.setrecursionlimit(10**8)

n, m, k = map(int, sys.stdin.readline().split())
candy = [0] + list(map(int, sys.stdin.readline().split()))
kids = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]

graph = defaultdict(list)
for a, b in kids:
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)

def dfs(start):
    visited[start] = True
    g_s = 1
    c_a = candy[start]

    for next in graph[start]:
        if not visited[next]:
            g_s_p, c_a_p = dfs(next)
            g_s += g_s_p
            c_a += c_a_p

    return g_s, c_a

group_list = []
for i in range(1, n + 1):
    if visited[i] == False:
        group_size, candy_amt = dfs(i)
        if group_size < k:
            group_list.append((group_size, candy_amt))

dp = [0] * k
for size, amt in group_list:
    for i in range(k-1, size - 1, -1):
        dp[i] = max(dp[i], dp[i - size] + amt)

print(dp[-1])

# ----------------------- 시간 초과 / BFS로 변경 --------------------------
import sys
from collections import defaultdict, deque

input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
k = int(data[2])

candy = [0] + list(map(int, data[3:n+3]))
kids = list(map(int, data[n+3:]))

graph = defaultdict(list)
for i in range(0, len(kids), 2):
    a = kids[i]
    b = kids[i+1]
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)

def bfs(start):
    queue = deque([start])
    visited[start] = True
    size = amt = 0

    while queue:
        now = queue.popleft()
        size += 1
        amt += candy[now]

        for next in graph[now]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True

    return size, amt

group_list = []
for i in range(1, n + 1):
    if visited[i] == False:
        group_size, candy_amt = bfs(i)
        if group_size < k:
            group_list.append((group_size, candy_amt))

dp = [[-1] * k for _ in range(len(group_list) + 1)]
dp[0][0] = 0

for i in range(1, len(group_list) + 1):
    group_size, candy_amt = group_list[i-1]
    for j in range(k):
        if dp[i-1][j] != -1:
            dp[i][j] = max(dp[i][j], dp[i-1][j])
        if j + group_size < k and dp[i-1][j] != -1:
            dp[i][j+group_size] = max(dp[i][j+group_size], dp[i-1][j] + candy_amt)

print(max(dp[-1]))

# ----------------------- 시간 초과 / find-union으로 변경... --------------------------
import sys
from collections import defaultdict
sys.setrecursionlimit(10**8)

n, m, k = map(int, sys.stdin.readline().split())
candy = [0] + list(map(int, sys.stdin.readline().split()))
kids = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)

    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

parent = list(range(n+1))
rank = [0] * (n+1)

for a, b in kids:
    union(parent, rank, a, b)

group_candy = [0] * (n + 1)
group_size = [0] * (n + 1)

for i in range(1, n + 1):
    root = find(parent, i)
    group_candy[root] += candy[i]
    group_size[root] += 1

dp_list = []
for i in range(1, n+1):
    if group_candy:
       dp_list.append((group_size[i], group_candy[i]))

dp = [0] * k
for size, amt in dp_list:
    for i in range(k - 1, size - 1, -1):
        dp[i] = max(dp[i], dp[i-size] + amt)

print(dp[-1])