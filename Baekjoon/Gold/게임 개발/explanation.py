import sys

n = int(sys.stdin.readline())
strategy = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

inform_dic, answer_time_dic = {}, {}
for i, inform_list in enumerate(strategy):
    inform_dic[i+1] = (inform_list[0], inform_list[1:-1])

def find_time(num):
    if num in answer_time_dic:
        return answer_time_dic[num]
    value = inform_dic[num][0]

    if inform_dic[num][1]:
        max_value = 0
        for sub_num in inform_dic[num][1]:
            max_value = max(max_value, find_time(sub_num))
        value += max_value
    answer_time_dic[num] = value
    return value

for i in range(1, n+1):
    print(find_time(i))