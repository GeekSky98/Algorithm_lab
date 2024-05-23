from heapq import heappop, heappush
def solution(prices):
    p_len = len(prices)
    answer = [float('inf')] * p_len

    before_queue = []
    for i, p in enumerate(prices):
        while before_queue and -before_queue[0][0] > p:
            _, b_i = heappop(before_queue)
            answer[b_i] = i - b_i
        heappush(before_queue, (-p, i))

    for _, l_i in before_queue:
        answer[l_i] = p_len - l_i - 1

    return answer