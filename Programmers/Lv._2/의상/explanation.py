from collections import defaultdict

def solution(clothes):
    c_dict = defaultdict(int)
    for _, type in clothes:
        c_dict[type] += 1
    answer = 1
    for value in c_dict.values():
        answer *= (value + 1)  # 안 입는 경우 추가

    return answer - 1