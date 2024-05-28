from heapq import heappush, heappop
def check_char(begin, target, char_len):
    same = 0
    for i in range(char_len):
        if begin[i] == target[i]:
            same += 1
    return True if same == char_len-1 else False

def solution(begin, target, words):
    if target not in words:
        return 0
    char_len = len(begin)
    queue = [(0, begin)]
    while queue:
        cost, now = heappop(queue)
        if now == target:
            return cost

        for word in words:
            if check_char(now, word, char_len):
                heappush(queue, (cost+1, word))

    return 0