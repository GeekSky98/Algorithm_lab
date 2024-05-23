from collections import defaultdict
def solution(N, number):
    if N == number:
        return 1

    dp = defaultdict(set)
    for i in range(1, 9):
        dp[i].add(int(str(N)*i))
        for j in range(1, i):
            for pp in dp[j]:
                for before in dp[i-j]:
                    dp[i].add(pp + before)
                    dp[i].add(pp - before)
                    dp[i].add(pp * before)
                    if before != 0:
                        dp[i].add(pp // before)
                    if number in dp[i]:
                        return i
    return -1