from heapq import heappush, heappop, heapify
def solution(n, works):
    if sum(works) <= n:
        return 0

    works = list(map(lambda x: -x, works))
    heapify(works)
    while n > 0:
        heappush(works, heappop(works) + 1)
        n -= 1

    return sum(map(lambda x: x**2, works))