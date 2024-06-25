import sys
farm = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]

def solution(n, f):
    answer = []
    for i in range(n):
        target_list_1 = f[i]
        target_list_2 = [f[j][i] for j in range(n)]
        for target in [target_list_1, target_list_2]:
            sorted_t = sorted(target)
            if sorted_t[0] == sorted_t[-1]:
                return 0
            answer.append((sorted_t[1]-sorted_t[0]) + (sorted_t[2]-sorted_t[1]))
    return min(answer)

print(solution(3,farm))