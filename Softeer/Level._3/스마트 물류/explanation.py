import sys

n, k = map(int, sys.stdin.readline().split())
line = list(sys.stdin.readline().strip())

visited = [False] * n
answer = 0

for index, target in enumerate(line):
    if target == "P":
        for i in range(max(0, index-k), min(n, index+k+1)):
            if line[i] == "H" and not visited[i]:
                answer += 1
                visited[i] = True
                break

print(answer)