from heapq import heappush, heappop, heapify
def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while len(scoville) > 1:
        num = heappop(scoville)
        if num >= K:
            return answer
        else:
            num2 = heappop(scoville)
            heappush(scoville, num+num2*2)
            answer += 1

    return answer if scoville[0] >= K else -1