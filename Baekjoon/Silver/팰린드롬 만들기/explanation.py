from collections import defaultdict

def solution(s):
    s_len = len(s)
    if s_len == 1:
        return s

    answer = ''
    check = ''
    count_dic = defaultdict(int)
    for i in range(s_len):
        count_dic[s[i]] += 1

    sorted_dic = sorted(count_dic.items(), key=lambda x: x[0])
    for key, value in sorted_dic:
        if value % 2 == 1:
            if check:
                return "I'm Sorry Hansoo"
            check = key
        for _ in range(value // 2):
            answer += key

    return answer + check + answer[::-1]

print(solution(input().strip()))
