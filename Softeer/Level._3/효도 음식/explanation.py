import sys
N = int(sys.stdin.readline().strip())
FOOD = list(map(int, sys.stdin.readline().split()))

def solution(n, food):
    if n == 3:
        return food[0] + food[-1]
    answer = -float('inf')

    dp_front = [-float('inf')] * n
    dp_back = [-float('inf')] * n

    sum_value = food[0]
    dp_front[0] = sum_value
    for i in range(1, n):
        sum_value = max(food[i], sum_value + food[i])
        dp_front[i] = max(dp_front[i-1], sum_value)

    sum_value = food[-1]
    dp_back[-1] = sum_value
    for j in range(n-2, -1, -1):
        sum_value = max(food[j], sum_value + food[j])
        dp_back[j] = max(dp_back[j+1], sum_value)

    for t in range(1, n-2):
        answer = max(answer, dp_front[t-1] + dp_back[t+1])

    return answer

print(solution(N, FOOD))