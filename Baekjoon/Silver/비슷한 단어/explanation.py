from collections import Counter

n = int(input())
target = input().strip()
voca = [input().strip() for _ in range(n-1)]

t_len = len(target)
target_dic = Counter(target)
target_set = set(target)
answer = 0
for v in voca:
    v_cnt = Counter(v)
    v_len = len(v)

    if abs(v_len - t_len) > 1:
        continue

    diff_cnt = 0
    for i in set(v) | target_set:
        diff_cnt += abs(target_dic[i] - v_cnt[i])

    if v_len == t_len and diff_cnt <= 2:
        answer += 1
    elif v_len != t_len and diff_cnt <= 1:
        answer += 1

print(answer)
