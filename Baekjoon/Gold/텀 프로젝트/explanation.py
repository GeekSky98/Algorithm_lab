import sys
sys.setrecursionlimit(10**6)

t = int(input())
test_case = []
for _ in range(t):
    temp = []
    temp.append(int(input()))
    temp.append([0] + list(map(int, input().split())))
    test_case.append(temp)

def dfs(s, t):
    global count
    visited[s] = True
    cycle_list.append(s)
    if visited[t[s]]:
        if t[s] in cycle_list:
            count -= len(cycle_list[cycle_list.index(t[s]):])
    else:
        dfs(t[s], t)

for n, t in test_case:
    visited = [False] * (n + 1)
    count = n
    for i in range(1, n + 1):
        if not visited[i]:
            cycle_list = []
            dfs(i, t)
    print(count)