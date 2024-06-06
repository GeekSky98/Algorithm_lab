import sys
n = int(sys.stdin.readline().strip())
train = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().strip())
target = list(map(int, sys.stdin.readline().split()))

def solution(n, m, train, target):
    train.sort(reverse=True)
    target.sort(reverse=True)
    if train[0] < target[0]:
        return -1

    answer = 0
    while target:
        answer += 1
        for t in train:
            if target and target[-1] > t:
                continue
            for i, b in enumerate(target):
                if t >= b:
                    target.pop(i)
                    break

    return answer

print(solution(n,m,train,target))