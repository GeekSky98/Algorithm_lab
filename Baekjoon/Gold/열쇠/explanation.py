import sys
from collections import deque, defaultdict

case_num = int(input())
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def solution(x, y, arr, key):
    key_set = set(key)
    future_dic = defaultdict(set)
    sides = []
    for i in range(x):
        for j in range(y):
            if i == 0 or i == x - 1 or j == 0 or j == y - 1:
                cell = arr[i][j]
                if cell != '*':
                    if "A" <= cell <= "Z":
                        if cell.lower() in key_set:
                            arr[i][j] = "."
                        else:
                            future_dic[cell.lower()].add((i, j))
                            continue

                    elif "a" <= cell <= "z":
                        key_set.add(cell)
                        arr[i][j] = "."

                    sides.append((i, j))

    if len(sides) == 0:
        return 0

    queue = deque()
    visited = [[False] * y for _ in range(x)]
    documents = 0
    for i, j in sides:
        if arr[i][j] == '$':
            documents += 1
        queue.append((i, j))
        visited[i][j] = True

    while queue:
        h, w = queue.popleft()

        if arr[h][w] == '$':
            documents += 1

        for dh, dw in directions:
            nh, nw = h + dh, w + dw
            if 0 <= nh < x and 0 <= nw < y and arr[nh][nw] != '*' and not visited[nh][nw]:
                cell = arr[nh][nw]
                if "A" <= cell <= "Z":
                    if cell.lower() in key_set:
                        queue.append((nh, nw))
                        visited[nh][nw] = True
                    else:
                        future_dic[cell.lower()].add((nh, nw))

                elif "a" <= cell <= "z":
                    key_set.add(cell)
                    arr[nh][nw] = "."
                    visited[nh][nw] = True
                    queue.append((nh, nw))
                    if cell in future_dic:
                        for fx, fy in future_dic[cell]:
                            if not visited[fx][fy]:
                                queue.append((fx, fy))
                                visited[fx][fy] = True
                        future_dic[cell] = set()

                else:
                    visited[nh][nw] = True
                    queue.append((nh, nw))

    return documents

for _ in range(case_num):
    x, y = map(int, input().split())
    arr = [list(map(str, list(sys.stdin.readline().strip()))) for _ in range(x)]
    key = list(map(str, input().strip()))
    if key[0] == "0":
        key = []
    print(solution(x, y, arr, key))