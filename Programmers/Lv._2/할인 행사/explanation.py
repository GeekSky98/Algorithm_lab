from collections import defaultdict

def solution(want, number, discount):
    discount_dic = defaultdict(int)
    for i in range(10):
        discount_dic[discount[i]] += 1

    w_len, d_len = len(want), len(discount)

    start_day = 1
    next_item = 10
    possible_cnt = 0
    while next_item <= d_len:
        if all(discount_dic[want[i]] >= number[i] for i in range(w_len)):
            possible_cnt += 1

        if next_item < d_len:
            discount_dic[discount[start_day - 1]] -= 1
            discount_dic[discount[next_item]] += 1

        start_day += 1
        next_item += 1

    return possible_cnt