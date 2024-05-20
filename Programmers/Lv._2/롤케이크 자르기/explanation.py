from collections import defaultdict
def solution(topping):
    answer = 0
    topping_len = len(topping)
    left_dic, right_dic = defaultdict(int), defaultdict(int)
    left_set, right_set = set(), set()
    for i in range(topping_len):
        left_set.add(topping[i])
        left_dic[i] = len(left_set)

    for i in range(topping_len-1, -1, -1):
        right_set.add(topping[i])
        right_dic[i] = len(right_set)

    for i in range(topping_len-1):
        if left_dic[i] == right_dic[i+1]:
            answer += 1
    return answer